// LuckySticks test in the Tilltown look: "One man was struck by lightning seven times". 9:16, voice and picture list from the posted Short.
import { E, registerShot, ease, prog, lerp, noise, text, FONTS } from '/engine/core.js';
import { drawToon, toonCard, LINE } from '/library/characters/toon.js';
import { RANGER } from '/library/characters/cast.js';
import { drawBear, drawFish, drawCat, drawClover } from '/library/characters/animals.js';
import { blueRidge } from '/library/worlds/blue-ridge.js';
import { dayStage } from '/library/sky/day.js';
import { lookoutTower, cabin } from '/library/buildings/park.js';
import { pickup } from '/library/vehicles/truck.js';
import { woodSign } from '/library/street-props/park.js';
import { bolt, flash, smoke, sparks, flame, dizzy, project, hit, blurBack } from '/library/effects/toon-fx.js';

// ---------- shared ----------
const ZAP = { ...RANGER, head: '#fff6a0', body: { ...RANGER.body, color: '#ffd93b' } };
const S = 3.36, FEET = 48, HEAD = 1.31, TOP = 1.63, HAT = 1.8, SHOULDER = 0.97, ANKLE = 0.05;
const HIPS = { front: [0.75, -1.95], back: [-0.75, 1.95] }, UP = { front: [2.75, 0.2], back: [-2.75, -0.2] };
function man(T, st, x, z, y = 0, W = 1024) { const c = toonCard(T, st, x, z, W, 1536, 2.4); c.mesh.position.y += y; c.ground = y; return c; }
function pose(c, o) { c.redraw((g, W, H) => drawToon(g, { x: W / 2, y: H - FEET, s: S, facing: 1, outfit: RANGER, ...o })); }
const at = (s, c, h) => project(s.T, s.stage.camera, c.mesh.position.x, c.ground + h, c.mesh.position.z);
const look = (cam, p, l) => { cam.position.set(...p); cam.lookAt(...l); };
const shake = (t, when, amp = 0.07) => { const k = hit(t, when, 0.45); return [noise(t * 37, 1) * amp * k, noise(t * 41, 7) * amp * k]; };
const blink = (t) => (t % 2.9) > 2.78;
function strike(g, t, when, x, y, seed = 1) { const k = hit(t, when, 0.42); if (k > 0) { bolt(g, t, x + 80, -40, x, y, { seed, a: Math.min(1, k * 2.6), w: 32 }); flash(g, k * k * 0.5); } sparks(g, x, y, t - when, { s: 1.5, seed }); }
const zapped = (t, when, d = 0.34) => t >= when && t < when + d;

function hud(g, n, age = 9) {
  const pop = 1 + 0.22 * Math.max(0, 1 - age / 0.22), cx = E.W / 2, y = 262;
  g.save(); g.translate(cx, y); g.scale(pop, pop);
  g.beginPath(); g.roundRect(-235, -56, 470, 112, 56); g.fillStyle = 'rgba(24,20,36,.9)'; g.fill(); g.lineWidth = 6; g.strokeStyle = '#ffd93b'; g.stroke();
  g.fillStyle = '#ffd93b'; g.beginPath(); for (const [px, py] of [[-178, -34], [-204, 8], [-184, 8], [-198, 40], [-156, -6], [-176, -6], [-158, -34]]) g.lineTo(px, py); g.closePath(); g.fill();
  text(g, `STRIKES: ${n}`, 26, 3, { size: 60, font: 'Montserrat', weight: 900, color: '#ffffff' });
  g.restore();
}
// builds one 3D shot; update(s, t, info) moves things, over(g, t, info, s) draws 2D on top
function shot(id, build, update, over) { registerShot(id, { kind: '3d', init(T) { const s = build(T); s.T = T; return s; }, draw(s, t, info) { update(s, t, info); }, overlay(g, t, info, s) { over?.(g, t, info, s); } }); }

const storm = (T, o = {}) => { const { stage } = blueRidge(T, { weather: 'storm', seed: 1, ...o }); return stage; };
const day = (T, o = {}) => { const { stage } = blueRidge(T, { weather: 'day', seed: 1, ...o }); return stage; };

// ---------- 1-3: the hook ----------
shot('s01', (T) => { const st = storm(T); return { stage: st, r: man(T, st, 0, 0) }; },
  (s, t, i) => { const k = ease.inOut(t / i.dur), [dx, dy] = shake(t, 0.62); look(s.stage.camera, [0.35 + dx, 1 + dy, lerp(4.6, 3.8, k)], [0.1, 2.5, -20]);
    const z = zapped(t, 0.62); pose(s.r, { outfit: z ? ZAP : RANGER, expr: t < 0.62 ? 'worried' : 'shocked', look: t < 0.62 ? [0, -1] : [0, 0], arms: t < 0.62 ? undefined : UP, bob: z ? noise(t * 50) * 10 : Math.sin(t * 3) * 1.5 }); s.r.face(s.stage.camera); },
  (g, t, i, s) => { const [x, y] = at(s, s.r, HAT); strike(g, t, 0.62, x, y, 1); });

const RING = [[-1.5, 0.3], [1.4, 0.8], [-0.7, -1.3], [1.8, -0.9], [-1.9, -0.8], [0.7, 1.5], [-0.2, 1.7]];
shot('s02', (T) => { const st = storm(T); return { stage: st, r: man(T, st, 0, 0) }; },
  (s, t, i) => { const k = ease.inOut(t / i.dur); look(s.stage.camera, [0.4, 1.5, lerp(5.6, 5.1, k)], [0, 2.1, -20]); pose(s.r, { expr: 'shocked', arms: UP, bob: noise(t * 30) * 5 }); s.r.face(s.stage.camera); },
  (g, t, i, s) => { let n = 0; RING.forEach(([x, z], k) => { const when = 0.08 + k * 0.2; if (t >= when) n = k + 1; const [px, py] = project(s.T, s.stage.camera, x, 0, z), a = hit(t, when, 0.28);
      if (t >= when) { g.save(); g.globalAlpha = 0.55; g.fillStyle = '#17131c'; g.beginPath(); g.ellipse(px, py, 62, 18, 0, 0, 7); g.fill(); g.restore(); }
      if (a > 0) { bolt(g, t, px + (k % 2 ? -60 : 60), -40, px, py, { seed: k + 2, a: 1, w: 24 }); flash(g, a * 0.22); } sparks(g, px, py, t - when, { seed: k + 3 }); });
    if (n) { const age = t - (0.08 + (n - 1) * 0.2), p = 1 + 0.3 * Math.max(0, 1 - age / 0.15); g.save(); g.translate(E.W / 2, 400); g.scale(p, p); text(g, String(n), 0, 0, { size: 260, font: 'Montserrat', weight: 900, color: '#ffd93b', stroke: 22, strokeColor: '#1d1a22' }); g.restore(); } });

shot('s03', (T) => { const st = storm(T); return { stage: st, r: man(T, st, 0, 0) }; },
  (s, t, i) => { const k = ease.inOut(t / i.dur); look(s.stage.camera, [lerp(0.4, 0.15, k), 1.05, lerp(4.2, 3.5, k)], [0, 2.3, -20]);
    pose(s.r, { expr: t > 0.55 ? 'happy' : 'neutral', blink: blink(t), bob: Math.sin(t * 3) * 1.6, arms: t > 0.55 ? { front: [2.1, -1.6], back: [-0.1, 0.05] } : undefined, prop: t > 0.55 ? (g, h) => { g.lineCap = 'round'; g.strokeStyle = LINE; g.lineWidth = 9; g.beginPath(); g.moveTo(h[0], h[1] - 6); g.lineTo(h[0], h[1] - 30); g.stroke(); g.strokeStyle = '#fff'; g.lineWidth = 4; g.stroke(); } : null }); s.r.face(s.stage.camera); },
  (g, t, i, s) => { const [x, y] = at(s, s.r, HAT); smoke(g, x, y, t, { count: 7, s: 1.5 }); });

// ---------- 4-5: who and where ----------
shot('s04', (T) => { const st = day(T), sign = woodSign(T, ['SHENANDOAH', 'NATIONAL PARK']); sign.position.set(-0.62, 0, -2.2); sign.rotation.y = 0.2; st.add(sign); return { stage: st, r: man(T, st, 0.72, 0) }; },
  (s, t, i) => { const k = ease.inOut(t / i.dur); look(s.stage.camera, [lerp(0.25, 0, k), 1.15, lerp(5.2, 4.7, k)], [0, 2.3, -20]); pose(s.r, { expr: 'happy', arms: HIPS, blink: blink(t), bob: Math.sin(t * 3) * 1.5, look: [-0.2, 0] }); s.r.face(s.stage.camera); });

shot('s05', (T) => { const st = day(T, { inner: 26 }); return { stage: st, r: man(T, st, 0, 0) }; },
  (s, t, i) => { const k = ease.inOut(t / i.dur); look(s.stage.camera, [0, lerp(3, 34, k), lerp(11, 34, k)], [0, lerp(7, 34, k), -300]); pose(s.r, { expr: 'happy', arms: { front: [2.9, 0.1], back: [-0.1, 0.05] } }); s.r.face(s.stage.camera); });

// ---------- 6-8: 1942, the lookout ----------
const TH = 14;
const towerWorld = (T) => { const st = storm(T, { inner: 22 }), tw = lookoutTower(T, { height: TH }); st.add(tw); return st; };
shot('s06', (T) => ({ stage: towerWorld(T) }),
  (s, t, i) => { const k = ease.inOut(t / i.dur); look(s.stage.camera, [lerp(5, 3.5, k), 1.3, lerp(19, 17, k)], [0, lerp(11, 12.5, k), 0]); });

shot('s07', (T) => { const st = towerWorld(T); return { stage: st, r: man(T, st, 0.5, 3.1, TH + 0.2) }; },
  (s, t, i) => { const k = ease.inOut(t / i.dur), [dx, dy] = shake(t, 0.59, 0.1); look(s.stage.camera, [lerp(2.6, 2.1, k) + dx, TH + 1.7 + dy, lerp(7.7, 7, k)], [0.4, TH + 1.75, 2]);
    const z = zapped(t, 0.59, 0.5); pose(s.r, { outfit: z ? ZAP : RANGER, expr: t < 0.59 ? 'neutral' : t < 1.5 ? 'ouch' : 'shocked', arms: t < 0.59 ? undefined : UP, bob: z ? noise(t * 50) * 10 : 0, blink: t < 0.59 && blink(t) }); s.r.face(s.stage.camera); },
  (g, t, i, s) => { const [x, y] = at(s, s.r, HAT); strike(g, t, 0.59, x, y, 8); smoke(g, x, y, t - 0.75, { count: 6, s: 1.5 }); if (t >= 0.59) hud(g, 1, t - 0.59); });

function boot(g, x, y, s, t, holed) {
  g.save(); g.translate(x, y); g.scale(s, s); g.lineJoin = 'round'; g.lineCap = 'round';
  g.strokeStyle = LINE; g.lineWidth = 36; g.beginPath(); g.moveTo(-52, -240); g.lineTo(-76, -760); g.stroke();
  g.beginPath(); g.moveTo(-150, -6); g.lineTo(230, -6); g.quadraticCurveTo(262, -46, 196, -96); g.bezierCurveTo(130, -128, 60, -132, 26, -160); g.lineTo(18, -262); g.lineTo(-122, -262); g.lineTo(-150, -70); g.closePath(); g.fillStyle = '#7a4f2e'; g.fill(); g.lineWidth = 9; g.stroke();
  g.beginPath(); g.moveTo(112, -116); g.quadraticCurveTo(150, -72, 128, -8); g.lineWidth = 6; g.stroke();
  g.beginPath(); g.rect(-164, -14, 410, 30); g.fillStyle = '#26212b'; g.fill(); g.lineWidth = 9; g.stroke();
  g.lineWidth = 6; g.strokeStyle = '#efe6d3'; for (let k = 0; k < 4; k++) { g.beginPath(); g.moveTo(-12 + k * 22, -232 + k * 26); g.lineTo(44 + k * 20, -212 + k * 26); g.stroke(); }
  if (holed) { g.fillStyle = '#ff8a2a'; g.beginPath(); g.ellipse(176, -74, 54, 34, 0.45, 0, 7); g.fill(); g.fillStyle = '#17131c'; g.beginPath(); g.ellipse(176, -74, 40, 24, 0.45, 0, 7); g.fill(); g.fillStyle = '#f7e9d0'; g.strokeStyle = LINE; g.lineWidth = 5; g.beginPath(); g.arc(178, -80 - Math.abs(Math.sin(t * 8)) * 7, 15, 0, 7); g.fill(); g.stroke(); }
  g.restore();
}
shot('s08', (T) => { const st = dayStage(T, { fov: 60 }); st.add(T.box(40, 0.2, 40, new T.THREE.MeshStandardMaterial({ map: T.planks('#a8835a', 14, [4, 4]), roughness: 1 }), 0, -0.1, 0)); return { stage: st }; },
  (s, t, i) => { look(s.stage.camera, [0.2, 3.6 - 0.25 * ease.inOut(t / i.dur), 1.6], [0.2, 0, 0]); },
  (g, t) => { const holed = t >= 0.75; boot(g, 470, 1090, 1.7 + 0.04 * t, t, holed); if (holed) { smoke(g, 790, 930, t - 0.75, { count: 8, s: 2.2 }); sparks(g, 790, 960, t - 0.75, { s: 2.2 }); flash(g, hit(t, 0.75, 0.22) * 0.5, '#ffb35a'); } hud(g, 1); });

// ---------- 9-10: 27 years later ----------
registerShot('s09', { draw(g, t, i) {
  g.fillStyle = '#a07a52'; g.fillRect(0, 0, E.W, E.H); for (let k = 0; k < 14; k++) { g.fillStyle = k % 2 ? 'rgba(0,0,0,.08)' : 'rgba(255,255,255,.05)'; g.fillRect(0, (k * E.H) / 14, E.W, E.H / 14); g.fillStyle = 'rgba(40,24,12,.5)'; g.fillRect(0, (k * E.H) / 14, E.W, 5); }
  const z = 1 + 0.05 * t; g.save(); g.translate(E.W / 2, 880); g.scale(z, z);
  const yr = (y) => { g.beginPath(); g.roundRect(-330, -420, 660, 840, 22); g.fillStyle = '#fdfaf2'; g.fill(); g.lineWidth = 9; g.strokeStyle = LINE; g.stroke(); g.save(); g.beginPath(); g.roundRect(-330, -420, 660, 190, 22); g.clip(); g.fillStyle = '#d6432f'; g.fillRect(-340, -430, 680, 200); g.restore(); text(g, 'YEAR', 0, -324, { size: 96, font: 'Montserrat', weight: 900, color: '#fff' }); text(g, String(y), 0, 90, { size: 230, font: 'Montserrat', weight: 900, color: '#26212b' }); };
  const prg = ease.inOut(Math.min(1, t / (i.dur * 0.82))), v = 27 * prg, cur = 1942 + Math.floor(v), q = v - Math.floor(v);
  yr(Math.min(1969, cur + (cur < 1969 ? 1 : 0)));
  if (cur < 1969) { g.save(); g.translate(q * 760, -q * 620); g.rotate(q * 1.2); g.globalAlpha = 1 - q * 0.4; yr(cur); g.restore(); } else { g.save(); yr(1969); g.restore(); }
  for (const x of [-210, 210]) { g.fillStyle = '#3a3640'; g.beginPath(); g.arc(x, -420, 20, 0, 7); g.fill(); }
  g.restore();
} });

shot('s10', (T) => ({ stage: storm(T, { road: true, inner: 26 }) }),
  (s, t, i) => { const k = ease.inOut(t / i.dur); look(s.stage.camera, [0.4, lerp(1.3, 1.9, k), lerp(22, 18, k)], [0, 11, -90]); },
  (g, t, i) => { const k = ease.out(t / i.dur), mass = (dir) => { g.fillStyle = '#39405c'; for (let n = 0; n < 11; n++) { const px = E.W / 2 + dir * (1250 - 780 * k) + dir * n * 56 - dir * 240, py = 110 + (n % 3) * 74 + Math.sin(n * 2.1) * 44, r = 150 + (n % 4) * 34; g.beginPath(); g.arc(px, py, r, 0, 7); g.fill(); } }; mass(-1); mass(1); const a = hit(t, 0.5, 0.25); if (a > 0) { bolt(g, t, 500, 200, 640, 1096, { seed: 21, a: 1, w: 16 }); flash(g, a * 0.18); } });

// ---------- 11-16: it keeps coming ----------
function truckAt(T, st, x, z, ry) { const p = pickup(T); p.position.set(x, 0, z); p.rotation.y = ry; st.add(p); return p; }
const toWorld = (s, group, x, y, z) => { const v = new s.T.THREE.Vector3(x, y, z); group.localToWorld(v); return project(s.T, s.stage.camera, v.x, v.y, v.z); };
shot('s11', (T) => { const st = storm(T, { road: true, inner: 26 }); return { stage: st, truck: truckAt(T, st, 0, 0, -1.1) }; },
  (s, t, i) => { const k = ease.inOut(t / i.dur), [dx, dy] = shake(t, 0.46, 0.12); look(s.stage.camera, [lerp(2.5, 2.1, k) + dx, 1.45 + dy, lerp(7.4, 6.6, k)], [0.1, 1.95, 0]); const a = hit(t, 0.46, 0.5); s.truck.position.y = a * Math.abs(Math.sin(t * 34)) * 0.1; s.truck.updateMatrixWorld(); },
  (g, t, i, s) => { const c = [[0.93, 1.24, 0.83], [0.93, 1.8, 0.83], [0.93, 1.8, -0.83], [0.93, 1.24, -0.83]].map(([x, y, z]) => toWorld(s, s.truck, x, y, z)), mid = toWorld(s, s.truck, 0.9, 1.5, 0.1), z = zapped(t, 0.46, 0.4);
    g.save(); g.beginPath(); c.forEach((p, n) => (n ? g.lineTo(...p) : g.moveTo(...p))); g.closePath(); g.clip(); drawToon(g, { x: mid[0], y: mid[1] + 250 * 0.92 - 8, s: 0.92, outfit: z ? ZAP : RANGER, expr: t < 0.46 ? 'neutral' : 'shocked', bob: z ? noise(t * 50) * 8 : 0 }); g.restore();
    const [x, y] = toWorld(s, s.truck, 0.2, 1.85, 0); strike(g, t, 0.46, x, y, 11); smoke(g, x, y, t - 0.65, { count: 6, s: 1.5 }); if (t >= 0.46) hud(g, 2, t - 0.46); else hud(g, 1); });

shot('s12', (T) => { const st = storm(T, { road: true, inner: 26 }); truckAt(T, st, 0, -3, -1.1); return { stage: st }; },
  (s, t, i) => { look(s.stage.camera, [1.5, 1.7, 9], [0, 2.4, -3]); },
  (g, t, i) => { blurBack(g, 11); const off = t >= 0.89, z = zapped(t, 0.23, 0.32), sc = 6.4 + 0.25 * t, y = 980 + 250 * sc;
    drawToon(g, { x: E.W / 2, y, s: sc, outfit: z ? ZAP : RANGER, expr: off ? 'neutral' : z ? 'ouch' : 'worried', noBrows: off, blink: off && (t % 1.2) > 1.08, bob: z ? noise(t * 50) * 5 : 0 });
    flash(g, hit(t, 0.23, 0.3) * 0.5);
    if (off) { const q = t - 0.89; for (const [dx, spin] of [[-95, -1], [147, 1]]) { g.save(); g.translate(E.W / 2 + dx + spin * q * 130, 868 + 900 * q * q + 220 * q); g.rotate(spin * q * 5); g.fillStyle = LINE; g.beginPath(); g.roundRect(-58, -13, 116, 26, 13); g.fill(); g.restore(); } smoke(g, E.W / 2 - 95, 850, q, { count: 4, s: 2 }); smoke(g, E.W / 2 + 147, 850, q, { count: 4, s: 2, seed: 9 }); }
    hud(g, 2); });

const yard = (T, sign) => { const st = storm(T), c = cabin(T, sign ? { sign } : {}); c.position.set(0, 0, -9); st.add(c); return st; };
shot('s13', (T) => { const st = yard(T); return { stage: st, r: man(T, st, 0.3, 0) }; },
  (s, t, i) => { const k = ease.inOut(t / i.dur), [dx, dy] = shake(t, 0.82); look(s.stage.camera, [lerp(0.7, 0.45, k) + dx, 1.2 + dy, lerp(5.2, 4.6, k)], [0.2, 2.2, -12]); const z = zapped(t, 0.82);
    pose(s.r, { outfit: z ? ZAP : RANGER, expr: t < 0.82 ? 'neutral' : 'ouch', blink: t < 0.82 && blink(t), arms: t < 0.82 ? undefined : { front: [2.3, -2.5], back: [-0.5, 0.3] }, bob: z ? noise(t * 50) * 9 : 0 }); s.r.face(s.stage.camera); },
  (g, t, i, s) => { const [x, y] = at(s, s.r, SHOULDER + 0.03); strike(g, t, 0.82, x + 72, y, 13); smoke(g, x + 72, y, t - 0.95, { count: 5, s: 1.3 }); if (t >= 0.82) hud(g, 3, t - 0.82); else hud(g, 2); });

shot('s14', (T) => { const st = yard(T, 'RANGER STATION'); return { stage: st, r: man(T, st, 0.1, 0) }; },
  (s, t, i) => { const k = ease.inOut(t / i.dur), [dx, dy] = shake(t, 0.64); look(s.stage.camera, [lerp(0.4, 0.2, k) + dx, 1.25 + dy, lerp(5.8, 5, k)], [0, 2.75, -12]); const z = zapped(t, 0.64);
    pose(s.r, { outfit: z ? ZAP : RANGER, hatOff: true, expr: t < 0.64 ? 'neutral' : 'shocked', blink: t < 0.64 && blink(t), arms: t < 0.64 ? undefined : UP, bob: z ? noise(t * 50) * 9 : Math.sin(t * 9) * 2 }); s.r.face(s.stage.camera); },
  (g, t, i, s) => { const [x, y] = at(s, s.r, TOP); strike(g, t, 0.64, x, y, 14); if (t >= 0.64) flame(g, t, x, y + 18, 2 * Math.min(1, (t - 0.64) / 0.14)); if (t >= 0.64) hud(g, 4, t - 0.64); else hud(g, 3); });

shot('s15', (T) => { const st = storm(T, { road: true, inner: 26 }); truckAt(T, st, -2.6, -3.4, -1.45); return { stage: st, r: man(T, st, 0.5, 0) }; },
  (s, t, i) => { const k = ease.inOut(t / i.dur); look(s.stage.camera, [0.7, 1.25, lerp(5, 4.5, k)], [0.1, 2.65, -12]);
    pose(s.r, { hatOff: true, expr: 'worried', look: [0, -1], arms: { front: [3.0, 0.35], back: [-0.1, 0.05] }, bob: Math.sin(t * 9) * 2,
      prop: (g, h) => { g.save(); g.translate(h[0] - 10, h[1] - 8); g.rotate(-2.2); g.beginPath(); g.moveTo(-30, -38); g.lineTo(30, -38); g.lineTo(24, 40); g.lineTo(-24, 40); g.closePath(); g.fillStyle = '#b9c2c8'; g.fill(); g.lineWidth = 4; g.strokeStyle = LINE; g.stroke(); g.restore(); } }); s.r.face(s.stage.camera); },
  (g, t, i, s) => { const [x, y] = at(s, s.r, TOP); const put = Math.min(1, t / 0.5); flame(g, t, x, y + 18, 2 * (1 - put * 0.85)); g.save(); g.strokeStyle = '#7fd0ff'; g.lineWidth = 12; g.lineCap = 'round'; for (let n = 0; n < 7; n++) { const dx = (n - 3) * 22 + Math.sin(t * 20 + n) * 6; g.beginPath(); g.moveTo(x + 60 + dx * 0.4, y - 120 + ((t * 900 + n * 60) % 40)); g.quadraticCurveTo(x + 20 + dx, y - 70, x + dx * 1.6, y + 40); g.stroke(); } g.restore(); smoke(g, x, y, t - 0.3, { count: 5, s: 1.5 }); hud(g, 5, t); });

shot('s16', (T) => { const st = storm(T); return { stage: st, r: man(T, st, 0, 0) }; },
  (s, t, i) => { const k = ease.inOut(t / i.dur), [dx, dy] = shake(t, 0.7); look(s.stage.camera, [lerp(0.3, 0.15, k) + dx, 1 + dy, lerp(4.4, 3.9, k)], [0, 2.1, -20]); const z = zapped(t, 0.7), after = t >= 0.7, hop = after ? Math.abs(Math.sin((t - 0.7) * 11)) * 0.34 : 0;
    s.r.mesh.position.y = 1.2 - 0.075 + hop; pose(s.r, { hatOff: false, outfit: z ? ZAP : RANGER, expr: after ? 'ouch' : 'neutral', arms: after ? UP : undefined, tilt: after ? Math.sin((t - 0.7) * 11) * 0.09 : 0 }); s.r.face(s.stage.camera); },
  (g, t, i, s) => { const [x, y] = at(s, s.r, ANKLE); strike(g, t, 0.7, x + 28, y, 16); smoke(g, x + 28, y, t - 0.82, { count: 4, s: 1.2 }); if (t >= 0.7) hud(g, 6, t - 0.7); else hud(g, 5); });

// ---------- 17-21: fishing ----------
const pondWorld = (T, weather) => blueRidge(T, { weather, seed: 1, pond: true, inner: 24 }).stage;
const rod = (g, h, tx, ty) => { g.lineCap = 'round'; g.strokeStyle = '#5a3f2a'; g.lineWidth = 6; g.beginPath(); g.moveTo(h[0], h[1]); g.lineTo(tx, ty); g.stroke(); };
const fishing = { front: [1.45, -0.5], back: [-0.1, 0.05] };
const floatLine = (g, tx, ty, bob) => { g.strokeStyle = 'rgba(245,245,245,.9)'; g.lineWidth = 2.5; g.beginPath(); g.moveTo(tx, ty); g.quadraticCurveTo(tx + 8, -70, 138, -36 + bob); g.stroke(); g.fillStyle = '#e8402f'; g.beginPath(); g.arc(138, -32 + bob, 10, 0, 7); g.fill(); g.lineWidth = 2.5; g.strokeStyle = LINE; g.stroke(); };

shot('s17', (T) => { const st = pondWorld(T, 'storm'); return { stage: st, r: man(T, st, -0.45, 1) }; },
  (s, t, i) => { const k = ease.inOut(t / i.dur); look(s.stage.camera, [lerp(0.4, 0.2, k), 1.5, lerp(7.2, 6.4, k)], [0, 2.8, -20]); pose(s.r, { expr: 'happy', blink: blink(t), bob: Math.sin(t * 2.4) * 1.5, arms: fishing, prop: (g, h) => { rod(g, h, 142, -300); floatLine(g, 142, -300, Math.sin(t * 3) * 3); } }); s.r.face(s.stage.camera); },
  (g, t) => hud(g, 6));

shot('s18', (T) => { const st = pondWorld(T, 'storm'); return { stage: st, r: man(T, st, -0.45, 1) }; },
  (s, t, i) => { const k = ease.inOut(t / i.dur), cast = ease.inOut(prog(t, 0.15, 0.7)), tipX = lerp(-40, 142, cast), tipY = lerp(-380, -300, cast); look(s.stage.camera, [0.2, 1.3, lerp(5.2, 4.8, k)], [0, 2.5, -20]);
    pose(s.r, { expr: 'happy', blink: blink(t), bob: Math.sin(t * 2.4) * 1.5, arms: { front: [lerp(2.6, 1.45, cast), -0.5], back: [-0.1, 0.05] }, prop: (g, h) => { rod(g, h, tipX, tipY); if (t > 0.72) floatLine(g, tipX, tipY, Math.sin(t * 8) * 6 * Math.max(0, 1.3 - (t - 0.72))); } }); s.r.face(s.stage.camera); },
  (g, t, i, s) => { hud(g, 6); if (t > 0.72) { const [x, y] = at(s, s.r, 0.08), u = Math.min(1, (t - 0.72) / 0.7); g.save(); g.strokeStyle = `rgba(255,255,255,${0.9 * (1 - u)})`; g.lineWidth = 5; g.beginPath(); g.ellipse(x + 300, y - 100, 30 + u * 170, 8 + u * 42, 0, 0, 7); g.stroke(); g.restore(); } });

shot('s19', (T) => { const st = pondWorld(T, 'storm'); return { stage: st, r: man(T, st, -0.2, 1) }; },
  (s, t, i) => { const k = ease.inOut(t / i.dur), [dx, dy] = shake(t, 0.64, 0.12); look(s.stage.camera, [-0.1 + dx, 1.25 + dy, lerp(4.8, 4.1, k)], [-0.2, 2.75, -20]); const z = zapped(t, 0.64, 0.46), after = t >= 0.64;
    pose(s.r, { hatOff: after, outfit: z ? ZAP : RANGER, expr: !after ? 'happy' : t < 1.5 ? 'ouch' : 'neutral', blink: !after && blink(t), bob: z ? noise(t * 50) * 11 : 0, arms: after ? UP : fishing, prop: after ? null : (g, h) => { rod(g, h, 142, -300); floatLine(g, 142, -300, Math.sin(t * 3) * 3); } }); s.r.face(s.stage.camera); },
  (g, t, i, s) => { const [x, y] = at(s, s.r, TOP); strike(g, t, 0.64, x, y, 19); smoke(g, x, y, t - 0.9, { count: 7, s: 1.6 }); if (t >= 0.64) { const q = t - 0.64, hx = x + q * 210, hy = y - 620 * q + 760 * q * q; g.save(); g.translate(hx, hy); g.rotate(q * 8); drawToon(g, { x: 0, y: 250 * 2.2 + 96, s: 2.2, outfit: { ...RANGER, head: 'rgba(0,0,0,0)', hair: null, body: { color: 'rgba(0,0,0,0)' } }, expr: 'neutral', noBrows: true, hatOnly: true }); g.restore(); hud(g, 7, q); } else hud(g, 6); });

const ranger2 = (t, hurtFace) => ({ hatOff: true, expr: hurtFace, blink: blink(t) });
const trout = (g, t) => { g.strokeStyle = 'rgba(245,245,245,.9)'; g.lineWidth = 2.5; g.beginPath(); g.moveTo(142, -326); g.lineTo(142, -262); g.stroke(); drawFish(g, 142, -212 + Math.sin(t * 6) * 4, 0.82, 1.57 + Math.sin(t * 9) * 0.25); };
shot('s20', (T) => { const st = pondWorld(T, 'day'); return { stage: st, r: man(T, st, -0.82, 1), b: toonCard(T, st, 2.6, 0.7, 1024, 1536, 2.4) }; },
  (s, t, i) => { const k = ease.inOut(t / i.dur), walk = ease.out(prog(t, 0.9, 1.9)), bx = lerp(2.6, 0.74, walk), grab = ease.inOut(prog(t, 1.9, 2.4)); look(s.stage.camera, [0.05, 1.2, lerp(6.1, 5.6, k)], [0.1, 2.2, -20]); s.b.mesh.position.x = bx;
    pose(s.r, { ...ranger2(t, t > 1.1 ? 'shocked' : 'neutral'), look: t > 1.1 ? [1, 0] : [0, 0], arms: { front: [2.2, -0.5], back: [-0.1, 0.05] }, prop: (g, h) => { rod(g, h, 142, -326); trout(g, t); } }); s.r.face(s.stage.camera);
    s.b.redraw((g, W, H) => drawBear(g, { x: W / 2, y: H - FEET, s: 2.9, facing: -1, reach: grab, bob: Math.sin(t * 8) * 4 })); s.b.face(s.stage.camera); },
  (g, t) => hud(g, 7));

shot('s21', (T) => { const st = pondWorld(T, 'day'), b = toonCard(T, st, 0.74, 0.7, 1024, 1536, 2.4); b.ground = 0; return { stage: st, r: man(T, st, -0.82, 1, 0, 1800), b }; },
  (s, t, i) => { const k = ease.inOut(t / i.dur), [dx, dy] = shake(t, 0.58, 0.1); look(s.stage.camera, [0.05 + dx, 1.2 + dy, lerp(5.6, 5.2, k)], [0.1, 2.2, -20]); const swing = ease.in(prog(t, 0.36, 0.58)), done = t > 0.58, knock = ease.out(prog(t, 0.58, 1.05));
    pose(s.r, { ...ranger2(t, 'angry'), arms: { front: [lerp(3.05, 1.5, swing), -0.1], back: [-0.5, 0.3] }, prop: (g, h) => { const a = lerp(3.3, 1.45, swing), L = 150, ex = h[0] + Math.sin(a) * L, ey = h[1] + Math.cos(a) * L; g.lineCap = 'round'; g.strokeStyle = LINE; g.lineWidth = 20; g.beginPath(); g.moveTo(h[0], h[1]); g.lineTo(ex, ey); g.stroke(); g.strokeStyle = '#8a5f38'; g.lineWidth = 12; g.stroke(); } }); s.r.face(s.stage.camera);
    s.b.mesh.position.x = lerp(0.74, 1.12, knock); s.b.redraw((g, W, H) => drawBear(g, { x: W / 2, y: H - FEET, s: 2.9, facing: -1, reach: done ? 0 : 1, hurt: done, bob: done ? Math.sin(t * 14) * 5 : Math.sin(t * 8) * 4 })); s.b.face(s.stage.camera); },
  (g, t, i, s) => { const [x, y] = at(s, s.b, 1.9); if (t > 0.58) { dizzy(g, t, x, y, 2); sparks(g, x, y + 90, t - 0.58, { s: 2 }); flash(g, hit(t, 0.58, 0.14) * 0.3); } hud(g, 7); });

// ---------- 22: the question ----------
shot('s22', (T) => { const st = day(T); return { stage: st, r: man(T, st, 0, 0) }; },
  (s, t, i) => { const k = ease.inOut(t / i.dur), clover = t > 0.2, cat = t > 0.75; look(s.stage.camera, [lerp(0.5, 0.15, k), 1.1, lerp(4.8, 4.2, k)], [0, 2.55, -20]);
    pose(s.r, { hatOff: true, expr: 'smirk', blink: blink(t), bob: Math.sin(t * 3) * 1.6, arms: { front: clover ? [2.2, -1.3] : [0.12, -0.05], back: [-0.1, 0.05] }, prop: (g, h) => { if (clover) drawClover(g, h[0] - 8, h[1] - 54, 0.85); if (cat) drawCat(g, { x: -112, y: 0, s: 0.72, facing: 1, bob: Math.sin(t * 4) * 8 }); } }); s.r.face(s.stage.camera); },
  (g, t, i, s) => { const [x, y] = at(s, s.r, TOP), p = ease.outBack(prog(t, 1.3, 1.65)); if (p > 0) { g.save(); g.translate(x, y - 300); g.scale(p, p); text(g, '?', 0, 0, { size: 460, font: 'Montserrat', weight: 900, color: '#ffd93b', stroke: 30, strokeColor: '#1d1a22' }); g.restore(); } });
