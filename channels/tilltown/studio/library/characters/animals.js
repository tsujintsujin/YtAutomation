// characters/animals.js — toon animals and small drawn things, same outline style as toon.js. Feet on y = 0, facing +x.
import { LINE } from '/library/characters/toon.js';

function out(g, path, fill, lw) { path(); if (fill) { g.fillStyle = fill; g.fill(); } g.lineWidth = lw; g.strokeStyle = LINE; g.lineJoin = 'round'; g.lineCap = 'round'; g.stroke(); }

// drawBear(g, { x, y, s, facing, reach (0..1), hurt (bool), bob })   standing on its hind legs
export function drawBear(g, o) {
  const fur = '#2d2931', light = '#7a6650', reach = o.reach || 0, b = o.bob || 0, lw = 4;
  g.save(); g.translate(o.x, o.y); g.scale((o.s ?? 1) * (o.facing ?? 1), o.s ?? 1);
  for (const x of [-40, 34]) out(g, () => { g.beginPath(); g.ellipse(x, -22, 34, 24, 0, 0, 7); }, fur, lw);
  const paw = (sx, sy, ex, ey) => { g.lineCap = 'round'; g.strokeStyle = LINE; g.lineWidth = 42; g.beginPath(); g.moveTo(sx, sy); g.lineTo(ex, ey); g.stroke(); g.strokeStyle = fur; g.lineWidth = 34; g.stroke(); out(g, () => { g.beginPath(); g.arc(ex, ey, 25, 0, 7); }, fur, lw); for (let k = -1; k <= 1; k++) { g.strokeStyle = '#e8e0d0'; g.lineWidth = 4; g.beginPath(); g.moveTo(ex + 18, ey + k * 12); g.lineTo(ex + 32, ey + k * 15); g.stroke(); } };
  paw(-44, -210 + b, -72, -130 + b);
  out(g, () => { g.beginPath(); g.ellipse(0, -140 + b, 88, 116, 0, 0, 7); }, fur, lw);
  out(g, () => { g.beginPath(); g.ellipse(14, -120 + b, 50, 72, 0, 0, 7); }, light, 3);
  const hy = -282 + b;
  for (const x of [-34, 58]) { out(g, () => { g.beginPath(); g.arc(x, hy - 48, 24, 0, 7); }, fur, lw); out(g, () => { g.beginPath(); g.arc(x, hy - 48, 11, 0, 7); }, light, 2.5); }
  out(g, () => { g.beginPath(); g.arc(12, hy, 66, 0, 7); }, fur, lw);
  out(g, () => { g.beginPath(); g.ellipse(36, hy + 22, 34, 25, 0, 0, 7); }, light, 3);
  g.fillStyle = '#100e14'; g.beginPath(); g.ellipse(42, hy + 10, 12, 8, 0, 0, 7); g.fill();
  if (o.hurt) { for (const x of [-4, 44]) { g.strokeStyle = '#ffffff'; g.lineWidth = 6; g.lineCap = 'round'; g.beginPath(); g.moveTo(x - 10, hy - 26); g.lineTo(x + 10, hy - 8); g.moveTo(x + 10, hy - 26); g.lineTo(x - 10, hy - 8); g.stroke(); } }
  else for (const x of [-2, 46]) { g.fillStyle = '#ffffff'; g.beginPath(); g.arc(x, hy - 17, 11, 0, 7); g.fill(); g.fillStyle = '#100e14'; g.beginPath(); g.arc(x + 3, hy - 16, 5.5, 0, 7); g.fill(); }
  g.strokeStyle = '#100e14'; g.lineWidth = 4; g.beginPath(); g.arc(38, hy + 24, 12, 0.3, 2.6); g.stroke();
  paw(44, -214 + b, 44 + 58 + reach * 40, -210 + b - reach * 26);
  g.restore();
}

export function drawFish(g, x, y, s = 1, rot = 0) {
  g.save(); g.translate(x, y); g.rotate(rot); g.scale(s, s);
  out(g, () => { g.beginPath(); g.moveTo(-58, 0); g.lineTo(-86, -24); g.lineTo(-82, 24); g.closePath(); }, '#7f9c8c', 3);
  out(g, () => { g.beginPath(); g.ellipse(0, 0, 66, 24, 0, 0, 7); }, '#a5bfae', 3.5);
  g.fillStyle = '#d9799a'; g.beginPath(); g.ellipse(-4, 5, 50, 7, 0, 0, 7); g.fill();
  g.fillStyle = '#4d6355'; for (const [a, b] of [[-34, -9], [-14, -12], [8, -11], [-24, 11]]) { g.beginPath(); g.arc(a, b, 3, 0, 7); g.fill(); }
  g.fillStyle = '#fff'; g.beginPath(); g.arc(42, -5, 7, 0, 7); g.fill(); g.fillStyle = LINE; g.beginPath(); g.arc(44, -5, 3.5, 0, 7); g.fill();
  g.restore();
}

export function drawCat(g, o) {
  const black = '#26222a', lw = 3.5, b = o.bob || 0;
  g.save(); g.translate(o.x, o.y); g.scale((o.s ?? 1) * (o.facing ?? 1), o.s ?? 1);
  g.lineCap = 'round'; g.strokeStyle = LINE; g.lineWidth = 15; g.beginPath(); g.moveTo(-34, -14); g.bezierCurveTo(-92, -24, -84, -112, -56, -116 - b); g.stroke(); g.strokeStyle = black; g.lineWidth = 9; g.stroke();
  out(g, () => { g.beginPath(); g.ellipse(-6, -52, 42, 54, 0, 0, 7); }, black, lw);
  const hy = -126;
  for (const s of [-1, 1]) out(g, () => { g.beginPath(); g.moveTo(s * 34, hy - 18); g.lineTo(s * 36, hy - 60); g.lineTo(s * 6, hy - 38); g.closePath(); }, black, lw);
  out(g, () => { g.beginPath(); g.ellipse(0, hy, 44, 38, 0, 0, 7); }, black, lw);
  for (const s of [-1, 1]) { g.fillStyle = '#ffd34d'; g.beginPath(); g.ellipse(s * 18, hy - 5, 11, 12, 0, 0, 7); g.fill(); g.fillStyle = '#100e14'; g.beginPath(); g.ellipse(s * 18, hy - 5, 3.5, 10, 0, 0, 7); g.fill(); }
  g.fillStyle = '#e88aa0'; g.beginPath(); g.moveTo(-5, hy + 10); g.lineTo(5, hy + 10); g.lineTo(0, hy + 17); g.closePath(); g.fill();
  g.restore();
}

export function drawClover(g, x, y, s = 1) {
  g.save(); g.translate(x, y); g.scale(s, s);
  g.strokeStyle = '#2f7a3a'; g.lineWidth = 7; g.lineCap = 'round'; g.beginPath(); g.moveTo(0, 0); g.quadraticCurveTo(8, 34, -6, 66); g.stroke();
  for (let i = 0; i < 4; i++) { g.save(); g.rotate((i * Math.PI) / 2 + Math.PI / 4); out(g, () => { g.beginPath(); g.moveTo(0, 0); g.bezierCurveTo(-34, -14, -38, -54, -13, -56); g.bezierCurveTo(-5, -57, 0, -50, 0, -44); g.bezierCurveTo(0, -50, 5, -57, 13, -56); g.bezierCurveTo(38, -54, 34, -14, 0, 0); }, '#4fb34e', 3.5); g.restore(); }
  g.restore();
}
