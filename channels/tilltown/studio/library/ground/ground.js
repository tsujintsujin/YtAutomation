// ground/ground.js — cobbled road, stone sidewalks, grass, gravel avenue.
// TRAP: never lay a huge ground sheet under nearer ground. Its depth values drift with the camera and it pokes through for
// a few frames (the road turned green at 3.2 s in the first test). grass() therefore starts past the street by default.
import { rng } from '/engine/core.js';

export function cobbles(T, rep) { return T.canvasTex(1024, 1024, (g, W, H) => {
  const r = rng(11), cols = ['#a99b88', '#9d8f7d', '#b5a793', '#91857a', '#a3937f'];
  g.fillStyle = '#6b6358'; g.fillRect(0, 0, W, H);
  const rows = 18, rh = H / rows, n = 16, sw = W / n;
  for (let j = -1; j <= rows; j++) for (let i = -1; i <= n; i++) {
    const x = i * sw + (j % 2 ? sw / 2 : 0) + 3, y = j * rh + 3, w = sw - 6, h = rh - 6;
    g.fillStyle = cols[Math.floor(r() * cols.length)]; g.beginPath(); g.roundRect(x, y, w, h, 12); g.fill();
    g.fillStyle = 'rgba(255,255,255,.16)'; g.beginPath(); g.roundRect(x + 6, y + 5, w - 12, h * 0.34, 8); g.fill();
    g.fillStyle = 'rgba(0,0,0,.12)'; g.beginPath(); g.roundRect(x + 4, y + h * 0.72, w - 8, h * 0.24, 6); g.fill();
  }
}, rep); }
export function slabs(T, rep) { return T.canvasTex(512, 512, (g, W, H) => {
  g.fillStyle = '#d6ccb9'; g.fillRect(0, 0, W, H); g.strokeStyle = 'rgba(90,80,65,.4)'; g.lineWidth = 4;
  for (let k = 0; k <= 4; k++) { g.beginPath(); g.moveTo(k * W / 4, 0); g.lineTo(k * W / 4, H); g.moveTo(0, k * H / 4); g.lineTo(W, k * H / 4); g.stroke(); }
}, rep); }

const std = (T, map) => new T.THREE.MeshStandardMaterial({ map, roughness: 1 });
export function road(T, st, { halfWidth = 6, len = 130, z = -35 } = {}) {
  const m = T.plane(halfWidth * 2, len, std(T, cobbles(T, [3, 26]))); m.rotation.x = -Math.PI / 2; m.position.set(0, 0.01, z); st.add(m);
}
export function sidewalks(T, st, { road: half = 6, street = 8.5, len = 130, z = -35 } = {}) {
  const w = street - half; for (const s of [-1, 1]) st.add(T.box(w, 0.16, len, std(T, slabs(T, [1, 40])), s * (half + w / 2), 0.08, z));
}
export function grass(T, st, { zStart = -70, color = '#6fb052' } = {}) {
  const m = T.plane(12000, 6000, T.mat(color)); m.rotation.x = -Math.PI / 2; m.position.set(0, -0.3, zStart - 3000); st.add(m);
}
export function avenue(T, st, { x = 10, width = 26, zStart = -100, len = 760, color = '#dccdaf' } = {}) {
  const m = T.plane(width, len, T.mat(color)); m.rotation.x = -Math.PI / 2; m.position.set(x, 0.02, zStart - len / 2); st.add(m);
}
