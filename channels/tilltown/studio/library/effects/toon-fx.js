// effects/toon-fx.js — cartoon effects drawn over a shot (lightning, flash, smoke, flames, sparks, dizzy stars).
// project() turns a 3D point into screen units, so a 2D bolt can land on a 3D character.
import { E, rng, clamp, alpha } from '/engine/core.js';

export function project(T, cam, x, y, z) { const v = new T.THREE.Vector3(x, y, z).project(cam); return [((v.x + 1) / 2) * E.W, ((1 - v.y) / 2) * E.H]; }

// strength of an event that happened at `at`: 1 at the hit, gone after `life` seconds; 0 before it
export const hit = (t, at, life = 0.4) => (t < at || t > at + life ? 0 : 1 - (t - at) / life);

// a jagged bolt from (x0, y0) to (x1, y1). It flickers: new shape every 2 frames.
export function bolt(g, t, x0, y0, x1, y1, { seed = 1, a = 1, w = 26 } = {}) {
  if (a <= 0) return;
  const r = rng(seed * 97 + Math.floor(t * 12)), n = 11, pts = [[x0, y0]], dx = x1 - x0, dy = y1 - y0, L = Math.hypot(dx, dy), nx = -dy / L, ny = dx / L;
  for (let i = 1; i < n; i++) { const u = i / n, off = (r() - 0.5) * L * 0.13 * (1 - u * 0.5); pts.push([x0 + dx * u + nx * off, y0 + dy * u + ny * off]); }
  pts.push([x1, y1]);
  const path = (lw, col) => { g.strokeStyle = col; g.lineWidth = lw; g.lineJoin = 'miter'; g.lineCap = 'round'; g.beginPath(); pts.forEach((p, i) => (i ? g.lineTo(...p) : g.moveTo(...p))); g.stroke(); };
  g.save(); g.globalAlpha *= a;
  g.save(); g.globalCompositeOperation = 'lighter'; path(w * 1.9, 'rgba(255,236,130,.2)'); g.restore();
  path(w + 10, '#2a2238'); path(w, '#ffd93b'); path(w * 0.42, '#fffbe0');
  g.restore();
}

export function flash(g, a, color = '#ffffff') { if (a <= 0) return; g.save(); g.setTransform(1, 0, 0, 1, 0, 0); g.fillStyle = alpha(color, clamp(a)); g.fillRect(0, 0, g.canvas.width, g.canvas.height); g.restore(); }

// cartoon smoke puffs rising from (x, y), started `age` seconds ago
export function smoke(g, x, y, age, { count = 5, s = 1, seed = 2 } = {}) {
  if (age < 0) return; const r = rng(seed);
  for (let i = 0; i < count; i++) {
    const delay = i * 0.13, dx = (r() - 0.5) * 60 * s, k = age - delay, R = (14 + r() * 16) * s; if (k < 0) continue; const u = (k % 1.3) / 1.3, rad = R * (0.6 + u * 1.5);
    g.save(); g.globalAlpha *= 1 - u * u; g.fillStyle = '#e9e7e2'; g.strokeStyle = '#2a2632'; g.lineWidth = 3.5 * s; g.beginPath(); g.arc(x + dx + Math.sin(k * 3 + i) * 12 * s, y - u * 170 * s, rad, 0, 7); g.fill(); g.stroke(); g.restore();
  }
}

// a flickering flame sitting on (x, y)
export function flame(g, t, x, y, s = 1) {
  const f = 1 + 0.12 * Math.sin(t * 31) + 0.08 * Math.sin(t * 47), lick = (h, w, col, dx = 0) => { g.fillStyle = col; g.strokeStyle = '#2a2238'; g.lineWidth = 4 * s; g.beginPath(); g.moveTo(x + dx - w * s, y); g.bezierCurveTo(x + dx - w * 1.2 * s, y - h * 0.5 * s * f, x + dx - w * 0.2 * s + Math.sin(t * 19) * 7 * s, y - h * 0.62 * s * f, x + dx + Math.sin(t * 23) * 9 * s, y - h * s * f); g.bezierCurveTo(x + dx + w * 0.35 * s, y - h * 0.62 * s * f, x + dx + w * 1.2 * s, y - h * 0.46 * s * f, x + dx + w * s, y); g.closePath(); g.fill(); };
  lick(120, 50, '#ff6a2a', -24); lick(150, 56, '#ff6a2a', 22); g.stroke(); lick(100, 40, '#ffa62b', -2); lick(62, 25, '#ffe36a', 2);
}

export function sparks(g, x, y, age, { count = 12, s = 1, seed = 3 } = {}) {
  if (age < 0 || age > 0.5) return; const r = rng(seed), u = age / 0.5;
  g.save(); g.lineCap = 'round'; for (let i = 0; i < count; i++) { const a = r() * 6.283, d0 = (30 + r() * 40) * s, d1 = d0 + (70 + r() * 110) * s * u; g.strokeStyle = i % 2 ? '#ffe36a' : '#ffffff'; g.lineWidth = (3 + r() * 3) * s; g.globalAlpha = 1 - u; g.beginPath(); g.moveTo(x + Math.cos(a) * d0, y + Math.sin(a) * d0); g.lineTo(x + Math.cos(a) * d1, y + Math.sin(a) * d1); g.stroke(); } g.restore();
}

export function dizzy(g, t, x, y, s = 1) {
  for (let i = 0; i < 3; i++) { const a = t * 6 + (i * 6.283) / 3, px = x + Math.cos(a) * 62 * s, py = y + Math.sin(a) * 16 * s; g.save(); g.translate(px, py); g.rotate(a); g.scale(s, s); g.fillStyle = '#ffd93b'; g.strokeStyle = '#2a2238'; g.lineWidth = 3; g.beginPath(); for (let k = 0; k < 10; k++) { const r = k % 2 ? 7 : 15, q = (k * Math.PI) / 5 - 1.57; g.lineTo(Math.cos(q) * r, Math.sin(q) * r); } g.closePath(); g.fill(); g.stroke(); g.restore(); }
}

// soft focus on what has been drawn so far, for close-ups over the world
export function blurBack(g, px = 12) { g.save(); g.setTransform(1, 0, 0, 1, 0, 0); g.filter = `blur(${px * E.PX}px)`; g.drawImage(g.canvas, 0, 0); g.restore(); }
