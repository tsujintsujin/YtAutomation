// buildings/park.js — wooden fire lookout tower and a ranger cabin. Both return a group to position.

function planks(T, base, rep) { return T.canvasTex(512, 512, (g, W, H) => { g.fillStyle = base; g.fillRect(0, 0, W, H); for (let i = 0; i < 12; i++) { g.fillStyle = i % 2 ? 'rgba(0,0,0,.07)' : 'rgba(255,255,255,.05)'; g.fillRect(0, (i * H) / 12, W, H / 12); g.fillStyle = 'rgba(30,18,10,.45)'; g.fillRect(0, (i * H) / 12, W, 3); } }, rep); }
function windowsTex(T, n = 4) { return T.canvasTex(512, 128, (g, W, H) => { g.fillStyle = '#8a6a44'; g.fillRect(0, 0, W, H); const w = W / n; for (let i = 0; i < n; i++) { const gl = g.createLinearGradient(0, 16, 0, H - 16); gl.addColorStop(0, '#8fbad8'); gl.addColorStop(1, '#3e6688'); g.fillStyle = gl; g.fillRect(i * w + 10, 16, w - 20, H - 32); g.fillStyle = '#efe6d3'; g.fillRect(i * w + w / 2 - 3, 16, 6, H - 32); g.fillRect(i * w + 10, H / 2 - 3, w - 20, 6); } }); }

// lookoutTower(T, { height }): the catwalk floor is at y = height + 0.2; a character stands at z = 3.2 in front of the cabin
export function lookoutTower(T, { height = 14 } = {}) {
  const { THREE } = T, g = new THREE.Group(), wood = T.mat('#7a5a3c'), dark = T.mat('#5c432d');
  const beam = (a, b, w, mat) => { const A = new THREE.Vector3(...a), B = new THREE.Vector3(...b), d = B.clone().sub(A), m = new THREE.Mesh(new THREE.BoxGeometry(w, d.length(), w), mat); m.position.copy(A.clone().add(B).multiplyScalar(0.5)); m.quaternion.setFromUnitVectors(new THREE.Vector3(0, 1, 0), d.normalize()); m.castShadow = true; g.add(m); };
  const at = (y) => 3.3 - (1.4 * y) / height;
  for (const sx of [-1, 1]) for (const sz of [-1, 1]) beam([sx * 3.3, 0, sz * 3.3], [sx * 1.9, height, sz * 1.9], 0.3, wood);
  const levels = [0.2, 0.42, 0.64, 0.86].map((k) => k * height);
  levels.forEach((y, i) => { const a = at(y), up = i < 3 ? levels[i + 1] : height, b = at(up);
    for (const s of [-1, 1]) { beam([-a, y, s * a], [a, y, s * a], 0.14, dark); beam([s * a, y, -a], [s * a, y, a], 0.14, dark); beam([-a, y, s * a], [b, up, s * b], 0.1, dark); beam([a, y, s * a], [-b, up, s * b], 0.1, dark); beam([s * a, y, -a], [s * b, up, b], 0.1, dark); beam([s * a, y, a], [s * b, up, -b], 0.1, dark); } });
  const H = height;
  g.add(T.box(7.4, 0.25, 7.4, new THREE.MeshStandardMaterial({ map: planks(T, '#9a7650', [2, 2]), roughness: 1 }), 0, H + 0.08, 0));
  const glass = new THREE.MeshStandardMaterial({ map: windowsTex(T), roughness: 0.6 });
  g.add(T.box(5, 1.1, 5, new THREE.MeshStandardMaterial({ map: planks(T, '#a07a52', [2, 1]), roughness: 1 }), 0, H + 0.75, 0), T.box(5.02, 1.25, 5.02, glass, 0, H + 1.95, 0));
  const roof = T.cone(4.6, 1.8, T.mat('#6d4a35', { flat: true }), 0, H + 3.45, 0, 4); roof.rotation.y = Math.PI / 4; g.add(roof);
  for (const s of [-1, 1]) { g.add(T.box(7.4, 0.08, 0.08, wood, 0, H + 1.25, s * 3.65), T.box(0.08, 0.08, 7.4, wood, s * 3.65, H + 1.25, 0)); for (let k = -3.6; k <= 3.6; k += 1.2) { g.add(T.box(0.08, 1.1, 0.08, wood, k, H + 0.7, s * 3.65), T.box(0.08, 1.1, 0.08, wood, s * 3.65, H + 0.7, k)); } }
  return g;
}

// cabin(T, { w, d, h, sign }): front wall faces +z
export function cabin(T, { w = 9, d = 6, h = 3, wall = '#8c5a3a', roof = '#4f5a48', sign = null } = {}) {
  const { THREE } = T, g = new THREE.Group(), wm = new THREE.MeshStandardMaterial({ map: planks(T, wall, [2, 1]), roughness: 1 });
  g.add(T.box(w, h, d, wm, 0, h / 2, 0));
  const sh = new THREE.Shape(); sh.moveTo(-w / 2 - 0.5, 0); sh.lineTo(w / 2 + 0.5, 0); sh.lineTo(0, 2.1); sh.closePath();
  // ridge runs along x: extrude a triangle of the depth instead
  const tri = new THREE.Shape(); tri.moveTo(-d / 2 - 0.5, 0); tri.lineTo(d / 2 + 0.5, 0); tri.lineTo(0, 1.9); tri.closePath();
  const r = new THREE.Mesh(new THREE.ExtrudeGeometry(tri, { depth: w + 0.8, bevelEnabled: false }), T.mat(roof, { flat: true })); r.rotation.y = Math.PI / 2; r.position.set(-w / 2 - 0.4, h, 0); r.castShadow = true; g.add(r);
  const glass = new THREE.MeshStandardMaterial({ map: windowsTex(T, 2), roughness: 0.6 });
  for (const x of [-w / 3.2, w / 3.2]) g.add(T.box(2.2, 1.2, 0.08, glass, x, h * 0.58, d / 2 + 0.02));
  g.add(T.box(1.2, 2.2, 0.1, T.mat('#4b3424'), 0, 1.1, d / 2 + 0.03), T.sphere(0.06, T.mat('#e0c070'), 0.42, 1.05, d / 2 + 0.1));
  if (sign) { const tex = T.canvasTex(768, 128, (c, W, H) => { c.fillStyle = '#5a3f2a'; c.fillRect(0, 0, W, H); c.strokeStyle = '#e8d7a8'; c.lineWidth = 6; c.strokeRect(8, 8, W - 16, H - 16); c.fillStyle = '#f2e4ba'; c.font = '700 66px Fredoka'; c.textAlign = 'center'; c.textBaseline = 'middle'; c.fillText(sign, W / 2, H / 2 + 3); }); g.add(T.box(4.6, 0.72, 0.1, new THREE.MeshStandardMaterial({ map: tex, roughness: 1 }), 0, h + 0.1, d / 2 + 0.34)); }
  return g;
}
