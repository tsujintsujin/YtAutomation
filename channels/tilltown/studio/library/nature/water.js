// nature/water.js — a round pond with ripples and a ring of shore rocks.
import { rng, shade } from '/engine/core.js';

export function pond(T, st, { x = 0, z = -9, r = 9, seed = 4 } = {}) {
  const { THREE } = T, R = rng(seed);
  const tex = T.canvasTex(1024, 1024, (g, W, H) => {
    const q = rng(seed + 1), gr = g.createRadialGradient(W / 2, H / 2, 40, W / 2, H / 2, W / 2); gr.addColorStop(0, '#2f7fb8'); gr.addColorStop(1, '#4fa6c9'); g.fillStyle = gr; g.fillRect(0, 0, W, H);
    g.lineCap = 'round'; for (let i = 0; i < 150; i++) { g.strokeStyle = `rgba(255,255,255,${0.1 + q() * 0.22})`; g.lineWidth = 2 + q() * 3; const px = q() * W, py = q() * H, L = 20 + q() * 70; g.beginPath(); g.moveTo(px, py); g.quadraticCurveTo(px + L / 2, py - 6, px + L, py); g.stroke(); }
  });
  const m = new THREE.Mesh(new THREE.CircleGeometry(r, 56), new THREE.MeshStandardMaterial({ map: tex, roughness: 0.35, metalness: 0.05 })); m.rotation.x = -Math.PI / 2; m.position.set(x, 0.05, z); m.receiveShadow = true; st.add(m);
  const geo = new THREE.IcosahedronGeometry(1, 0);
  for (let i = 0; i < 80; i++) { const a = (i / 80) * 6.283 + R() * 0.08, k = r + 0.05 + R() * 0.35, s = 0.1 + R() * 0.2, c = new THREE.Mesh(geo, T.mat(shade('#8f8f92', (R() - 0.5) * 0.3), { flat: true })); c.scale.set(s, s * 0.7, s); c.position.set(x + Math.cos(a) * k, s * 0.3, z + Math.sin(a) * k); c.rotation.set(R() * 3, R() * 3, 0); c.castShadow = true; c.receiveShadow = true; st.add(c); }
}
