// The runner: holds one connection to the bridge (127.0.0.1:8766), takes the commands n8n sends, carries each
// one out in Chrome, and answers. It decides nothing and remembers nothing: which windows, which accounts, which
// image goes where, and which accounts are on limit are all n8n's. Every command acts on exactly the list it gets.
//   setup          {}                         -> closes every other runner tab, Gemini tab and image tab
//   listWindows    { windowIds }              -> { open: [windowIds that still have a Gemini tab] }
//   openWindows    { accounts }               -> { opened: { account: windowId } }
//   prompt         { slug, jobs:[{windowId, id}] } -> { sent: { windowId: {id, sent} | {id, error} }, sentAt }
//   look           { windowIds }              -> { found: { windowId: {src} | {limit} | {waiting} | {gone} | {robotCheck} } }
//   openTabs       { jobs:[{windowId, url}] }  -> { tabIds }
//   saveImages     { slug, jobs:[{windowId, id, src}] } -> { saved: [ids], errors: { id: error } }
//   closeTabs      { tabIds }                 -> {}
//   switchAccounts { jobs:[{windowId, account}] } -> {}
//   newChat        { jobs:[{windowId, account}] } -> {}   a new chat for that account
const BRIDGE = 'http://127.0.0.1:8766';
const get = p => fetch(BRIDGE + p).then(r => r.json());
const post = (p, body) => fetch(BRIDGE + p, { method: 'POST', body: JSON.stringify(body) }).then(r => r.json());
const chatUrl = acct => `https://gemini.google.com/app?authuser=${encodeURIComponent(acct)}`;
const log = s => {
  const el = document.getElementById('log');
  el.textContent = (new Date().toLocaleTimeString() + ' ' + s + '\n' + el.textContent).slice(0, 20000);
};

const COMMANDS = { setup, listWindows, openWindows, prompt, look, openTabs, saveImages, closeTabs, switchAccounts, newChat };

// The connection: ask the bridge for the next command (it holds the request open until there is one),
// carry it out, answer, ask again.
(async function listen() {
  for (;;) {
    let cmd;
    try {
      cmd = await get('/cmd');
    } catch (e) {                                                   // bridge not running: try again shortly
      await new Promise(r => setTimeout(r, 5000));
      continue;
    }
    if (!cmd.id) continue;
    log(`${cmd.name} ${JSON.stringify(cmd.args).slice(0, 200)}`);
    let ans;
    try {
      if (!COMMANDS[cmd.name]) throw new Error('unknown command ' + cmd.name);
      ans = Object.assign({ ok: true }, await COMMANDS[cmd.name](cmd.args || {}));
    } catch (e) {
      ans = { ok: false, error: String(e && e.stack || e) };
    }
    log(`${cmd.name} -> ${JSON.stringify(ans).slice(0, 300)}`);
    await post('/result', Object.assign(ans, { id: cmd.id })).catch(e => log('answer failed: ' + e));
  }
})();

const windowTab = async winId => {
  const w = await chrome.windows.get(winId, { populate: true }).catch(() => null);
  return w && w.tabs.find(t => /gemini\.google\.com/.test(t.url || t.pendingUrl || ''));
};
const inPage = async (tabId, func, args = []) =>
  (await chrome.scripting.executeScript({ target: { tabId }, func, args }).catch(e => [{ result: { error: String(e) } }]))[0].result;
// Every command works on all its windows at the same time; no window waits for another.
const each = (list, fn) => Promise.all(list.map(fn));
// For actions that reach Google (opening a page, sending a prompt): each window first waits its own random 1-3 s,
// so the windows never hit Google at the same instant.
const sleep = ms => new Promise(r => setTimeout(r, ms));
const eachStaggered = (list, fn) => each(list, async (x, i) => { await sleep(1000 + Math.random() * 2000); return fn(x, i); });
// Google's robot check: the window's page has been sent to google.com/sorry.
const robotCheck = async winId => {
  const w = await chrome.windows.get(winId, { populate: true }).catch(() => null);
  return !!w && w.tabs.some(t => /^https:\/\/(www\.)?google\.[a-z.]+\/sorry/.test(t.url || t.pendingUrl || ''));
};
const loaded = tabId => new Promise(res => {
  const f = (id, info) => { if (id === tabId && info.status === 'complete') { chrome.tabs.onUpdated.removeListener(f); res(); } };
  chrome.tabs.onUpdated.addListener(f);
  setTimeout(() => { chrome.tabs.onUpdated.removeListener(f); res(); }, 30000);
});

// Close every other runner tab, every Gemini tab and every leftover image tab (blob:https://gemini.google.com/...,
// opened by step 4). A window left empty closes with its last tab.
async function setup() {
  const me = (await chrome.tabs.getCurrent()).id;
  const runners = (await chrome.tabs.query({ url: chrome.runtime.getURL('runner.html') })).filter(t => t.id !== me);
  const gemini = (await chrome.tabs.query({})).filter(t =>
    /^https:\/\/gemini\.google\.com\/|^blob:https:\/\/gemini\.google\.com\//.test(t.url || t.pendingUrl || ''));
  await each([...runners, ...gemini], t => chrome.tabs.remove(t.id).catch(() => {}));
  return { closedRunners: runners.length, closedTabs: gemini.length };
}

async function listWindows({ windowIds }) {
  const open = [];
  await each(windowIds, async id => { if (await windowTab(id)) open.push(id); });
  return { open };
}

async function openWindows({ accounts }) {
  const opened = {};
  await eachStaggered(accounts, async acct => {
    const w = await chrome.windows.create({ url: chatUrl(acct), focused: false });
    opened[acct] = w.id;
    await loaded(w.tabs[0].id);
  });
  return { opened };
}

async function prompt({ slug, jobs }) {
  const refs = jobs.length ? await get(`/refs?slug=${encodeURIComponent(slug)}`) : [];
  const sent = {};
  await eachStaggered(jobs, async ({ windowId, id }) => {
    if (await robotCheck(windowId)) { sent[windowId] = { id, error: 'Google robot check', robotCheck: true }; return; }
    const tab = await windowTab(windowId);
    if (!tab) { sent[windowId] = { id, error: 'no Gemini tab in this window' }; return; }
    const { text } = await get(`/prompt?slug=${encodeURIComponent(slug)}&id=${id}`);
    sent[windowId] = Object.assign({ id }, await inPage(tab.id, sendPrompt, [text, refs]));
  });
  return { sent, sentAt: Date.now() };
}

async function sendPrompt(text, refs) {
  const sleep = ms => new Promise(r => setTimeout(r, ms));
  const waitFor = async (fn, ms) => { for (let t = 0; t < ms; t += 250) { const v = fn(); if (v) return v; await sleep(250); } return null; };
  const ed = await waitFor(() => document.querySelector('rich-textarea .ql-editor'), 30000);
  if (!ed) return { error: 'input box not found' };
  const menu = [...document.querySelectorAll('button')].find(b => /^upload/i.test(b.getAttribute('aria-label') || ''));
  if (!menu) return { error: 'Upload button not found' };
  const imgInput = () => [...document.querySelectorAll('input[type=file]')].find(i => i.accept === 'image/*');
  if (!imgInput()) menu.click();                               // the menu is a toggle: click only if closed
  const input = await waitFor(imgInput, 5000);
  if (!input) return { error: 'image input not found' };
  const dt = new DataTransfer();
  refs.forEach(r => dt.items.add(new File([Uint8Array.from(atob(r.b64), c => c.charCodeAt(0))], r.name, { type: 'image/jpeg' })));
  input.files = dt.files;
  input.dispatchEvent(new Event('change', { bubbles: true }));
  await sleep(500);
  if (imgInput()) menu.click();                                // close the menu again
  ed.focus();
  document.execCommand('selectAll');
  document.execCommand('insertText', false, text);
  const send = await waitFor(() => {                           // enabled once the 3 uploads are done
    const b = [...document.querySelectorAll('button')].find(b => /^send/i.test(b.getAttribute('aria-label') || ''));
    return b && !b.disabled && b.getAttribute('aria-disabled') !== 'true' && b;
  }, 60000);
  if (!send) return { error: 'send button never enabled' };
  send.click();
  return { sent: true };
}

// Look once: does the last answer have a loaded "AI generated" image, or say the limit is reached? Also reports
// the image number in the prompt above that answer ("(image NNN)"), so n8n can tell a new answer from an old one.
async function look({ windowIds }) {
  const found = {};
  await each(windowIds, async windowId => {
    if (await robotCheck(windowId)) { found[windowId] = { robotCheck: true }; return; }
    const tab = await windowTab(windowId);
    if (!tab) { found[windowId] = { gone: true }; return; }
    found[windowId] = await inPage(tab.id, () => {
      const resp = [...document.querySelectorAll('model-response')].pop();
      const box = resp && (resp.closest('.conversation-container') || resp.parentElement);
      const tag = box && box.querySelector('user-query')?.textContent.match(/\(image (\d{3})\)/);
      const forImage = tag ? +tag[1] : null;
      if (resp) {
        const img = [...resp.querySelectorAll('img')].find(i => /AI generated/i.test(i.alt || '') && i.classList.contains('loaded'));
        if (img) return { src: img.src, forImage };
        if (/limit resets|create more images as soon as your limit/i.test(resp.innerText)) return { limit: true, forImage };
      }
      return { waiting: true, forImage };
    });
  });
  return { found };
}

async function openTabs({ jobs }) {
  const tabIds = [];
  await each(jobs, async ({ windowId, url }) => tabIds.push((await chrome.tabs.create({ windowId, url, active: false })).id));
  return { tabIds };
}

// Save the image at src (read inside its window's Gemini page) as img/NNN.jpg, NNN = the id n8n gives.
async function saveImages({ slug, jobs }) {
  const saved = [], errors = {};
  await each(jobs, async ({ windowId, id, src }) => {
    const tab = await windowTab(windowId);
    const out = tab ? await inPage(tab.id, async src => {
      const blob = await (await fetch(src)).blob();
      const b64 = await new Promise(ok => { const f = new FileReader(); f.onload = () => ok(String(f.result).split(',')[1]); f.readAsDataURL(blob); });
      return { b64 };
    }, [src]) : { error: 'no Gemini tab in this window' };
    if (out.error) { errors[id] = out.error; return; }
    const ack = await post(`/image?slug=${encodeURIComponent(slug)}`, { id, b64: out.b64 });
    if (ack.ok) saved.push(id); else errors[id] = ack.error;
  });
  return { saved, errors };
}

async function closeTabs({ tabIds }) {
  await each(tabIds, id => chrome.tabs.remove(id).catch(() => {}));
  return {};
}

async function switchAccounts({ jobs }) {
  await eachStaggered(jobs, async ({ windowId, account }) => {
    const tab = await windowTab(windowId);
    if (tab) await chrome.tabs.update(tab.id, { url: chatUrl(account) });
  });
  return {};
}

// Go to a new chat for the window's account (a full page load, so no separate refresh).
async function newChat({ jobs }) {
  await eachStaggered(jobs, async ({ windowId, account }) => {
    const tab = await windowTab(windowId);
    if (!tab) return;
    await chrome.tabs.update(tab.id, { url: chatUrl(account) });
    await loaded(tab.id);
  });
  return {};
}
