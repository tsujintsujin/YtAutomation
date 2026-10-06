// Keeps the runner tab open. The runner (runner.html) holds the connection to the bridge (127.0.0.1:8766) and
// carries out the commands n8n sends; this file does nothing else.
const RUNNER = chrome.runtime.getURL('runner.html');

async function openRunner() {
  const [have] = await chrome.tabs.query({ url: RUNNER });
  if (have) return;
  const t = await chrome.tabs.create({ url: RUNNER, pinned: true, active: false });
  await chrome.tabs.update(t.id, { autoDiscardable: false });     // Chrome's Memory Saver must not unload it
}

chrome.runtime.onInstalled.addListener(openRunner);
chrome.runtime.onStartup.addListener(openRunner);
chrome.tabs.onRemoved.addListener(openRunner);                     // closed: open it again, it is the connection
