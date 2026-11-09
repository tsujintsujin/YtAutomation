// buildings/haussmann.js — Paris apartment blocks: stone facades, balconies, shopfronts, mansard roofs, dormers, chimneys.
// Only the street-facing side has the detailed facade. Change `seed` for a different-looking row.
import { rng, shade } from '/engine/core.js';

export function facadeTex(T, o) {
  const { stone = '#eadfc8', shop = '#2f5a4a', cafe = false, cols = 5, seed = 1 } = o;
  return T.canvasTex(1024, 1536, (g, W, H) => {
    const r = rng(seed);
    g.fillStyle = stone; g.fillRect(0, 0, W, H);
    g.strokeStyle = 'rgba(120,100,70,.18)'; g.lineWidth = 2; for (let y = 0; y < H; y += 34) { g.beginPath(); g.moveTo(0, y); g.lineTo(W, y); g.stroke(); }
    const groundH = H * 0.2, floors = 5, top = 64, fh = (H - groundH - top) / floors, cw = W / cols;
    g.fillStyle = shade(stone, -0.14); g.fillRect(0, 0, W, 44); g.fillStyle = shade(stone, -0.3); for (let x = 6; x < W; x += 28) g.fillRect(x, 44, 14, 14);
    for (let j = 0; j < floors; j++) for (let i = 0; i < cols; i++) {
      const wx = i * cw + cw * 0.24, wy = top + j * fh + fh * 0.13, ww = cw * 0.52, wh = fh * 0.68;
      if (j === 3) { g.fillStyle = shade(stone, -0.1); g.beginPath(); g.moveTo(wx - 16, wy - 10); g.lineTo(wx + ww / 2, wy - 42); g.lineTo(wx + ww + 16, wy - 10); g.closePath(); g.fill(); }
      g.fillStyle = '#f7f1e4'; g.fillRect(wx - 9, wy - 9, ww + 18, wh + 18);
      const gl = g.createLinearGradient(0, wy, 0, wy + wh); gl.addColorStop(0, '#79a2c6'); gl.addColorStop(1, '#3a5e82'); g.fillStyle = gl; g.fillRect(wx, wy, ww, wh);
      g.fillStyle = 'rgba(255,255,255,.26)'; g.beginPath(); g.moveTo(wx, wy + wh * 0.5); g.lineTo(wx + ww * 0.55, wy); g.lineTo(wx + ww * 0.85, wy); g.lineTo(wx, wy + wh * 0.8); g.closePath(); g.fill();
      g.fillStyle = '#f7f1e4'; g.fillRect(wx + ww / 2 - 3, wy, 6, wh); g.fillRect(wx, wy + wh * 0.38 - 3, ww, 6);
      if (r() < 0.3) { g.fillStyle = 'rgba(245,235,215,.8)'; g.fillRect(wx + 3, wy + 3, ww * 0.2, wh - 6); g.fillRect(wx + ww - 3 - ww * 0.2, wy + 3, ww * 0.2, wh - 6); }   // curtains
    }
    for (const j of [3, 0]) {                                     // wrought-iron balconies
      const y = top + j * fh + fh * 0.86; g.fillStyle = '#2b2a31'; g.fillRect(0, y - 40, W, 6); g.fillRect(0, y, W, 6); for (let x = 2; x < W; x += 13) g.fillRect(x, y - 40, 3.5, 44);
    }
    const gy = H - groundH; g.fillStyle = shop; g.fillRect(0, gy, W, groundH);          // shopfront
    g.fillStyle = shade(shop, 0.18); g.fillRect(0, gy, W, 16);
    for (let i = 0; i < cols; i++) {
      const wx = i * cw + cw * 0.1, ww = cw * 0.8, wy = gy + 62, wh = groundH - 100;
      const gl = g.createLinearGradient(0, wy, 0, wy + wh); gl.addColorStop(0, cafe ? '#ffd98f' : '#8fb2cf'); gl.addColorStop(1, cafe ? '#c98a3e' : '#46688a'); g.fillStyle = gl; g.fillRect(wx, wy, ww, wh);
      g.fillStyle = 'rgba(255,255,255,.2)'; g.fillRect(wx + 8, wy + 6, ww * 0.18, wh - 12);
      g.fillStyle = shade(shop, -0.3); g.fillRect(wx - 5, wy - 5, ww + 10, 5); g.fillRect(wx - 5, wy + wh, ww + 10, 5); g.fillRect(wx - 5, wy, 5, wh); g.fillRect(wx + ww, wy, 5, wh);
    }
    if (cafe) { g.fillStyle = '#f5e6b8'; g.font = '700 46px Fredoka'; g.textAlign = 'center'; g.textBaseline = 'middle'; g.fillText('CAFÉ', W / 2, gy + 38); }
  });
}

// one block on the left (side -1) or right (side 1) of a street whose facades stand at x = ±street
export function block(T, st, { side, street = 8.5, z0, len, h, tex, roof = '#7f8da0', seed = 1 }) {
  const { THREE } = T, depth = 14, xc = side * (street + depth / 2), r = rng(seed);
  const face = new THREE.MeshStandardMaterial({ map: tex, roughness: 1 }), wall = T.mat('#e0d3bb');
  const b = new THREE.Mesh(new THREE.BoxGeometry(depth, h, len), side < 0 ? [face, wall, wall, wall, wall, wall] : [wall, face, wall, wall, wall, wall]);
  b.position.set(xc, h / 2, z0 - len / 2); b.castShadow = b.receiveShadow = true; st.add(b);
  const sh = new THREE.Shape(); sh.moveTo(0, 0); sh.lineTo(depth, 0); sh.lineTo(depth - 1.8, 4); sh.lineTo(1.8, 4); sh.closePath();
  const m = new THREE.Mesh(new THREE.ExtrudeGeometry(sh, { depth: len, bevelEnabled: false }), T.mat(roof, { flat: true })); m.position.set(xc - depth / 2, h, z0 - len); m.castShadow = true; st.add(m);
  for (let z = z0 - 2; z > z0 - len + 1; z -= 3.4) {
    const x = side * (street + 1.0);
    st.add(T.box(1.3, 1.9, 1.4, '#efe6d3', x, h + 1.5, z), T.box(0.08, 1.05, 0.85, '#4d7196', x - side * 0.68, h + 1.45, z));
  }
  for (let z = z0 - 4; z > z0 - len; z -= 6 + r() * 2) st.add(T.box(1.3, 2.6, 0.8, '#b5654a', xc + side * 1, h + 5, z));
}

export const ROW_LENGTHS = [20, 16, 20, 18, 20];
const STONES = ['#eadfc8', '#e4d6bb', '#efe5d2', '#e2d2b6'], SHOPS = ['#2f5a4a', '#7a2f2a', '#2f4a72', '#5a4a2e'];
// both sides of a street, blocks running from z0 toward -z. cafeAt: which left block has the café front (-1 for none).
export function haussmannRow(T, st, { street = 8.5, z0 = 18, lengths = ROW_LENGTHS, cafeAt = 1, seed = 0 } = {}) {
  let zL = z0, zR = z0;
  lengths.forEach((len, i) => {
    const cafe = i === cafeAt, k = i + seed;
    block(T, st, { side: -1, street, z0: zL, len, h: 20 + (i % 2) * 1.2, tex: facadeTex(T, { stone: STONES[k % 4], shop: cafe ? '#7a2f2a' : SHOPS[k % 4], cafe, seed: 3 + k }), seed: 3 + k }); zL -= len;
    block(T, st, { side: 1, street, z0: zR, len, h: 21 - (i % 2), tex: facadeTex(T, { stone: STONES[(k + 2) % 4], shop: SHOPS[(k + 1) % 4], seed: 9 + k }), roof: '#73829a', seed: 9 + k }); zR -= len;
  });
}

// a hazy row of low blocks on the far horizon
export function farSkyline(T, st, { seed = 5, count = 40 } = {}) {
  const r = rng(seed); for (let i = 0; i < count; i++) st.add(T.box(40 + r() * 50, 18 + r() * 26, 30, T.mat('#c2c9d4'), -1000 + i * 52 + r() * 20, 14, -1250 - r() * 150));
}
