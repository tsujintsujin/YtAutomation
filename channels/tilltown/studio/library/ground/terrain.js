// ground/terrain.js — grassy land that is flat around the origin and rolls away from it, grass tufts, a dirt road.
// meadow() returns heightAt(x, z) so things can be placed on the land. It is the only ground sheet (see the trap in ground.js).
import { rng, shade } from '/engine/core.js';

function grassTex(T, rep) { return T.canvasTex(1024, 1024, (g, W, H) => {
  const r = rng(7), cols = ['#5da346', '#6fb552', '#4f9440', '#7cc05c', '#58a04a'];
  g.fillStyle = '#5ea548'; g.fillRect(0, 0, W, H);
  for (let i = 0; i < 40; i++) { g.fillStyle = 'rgba(40,90,40,.1)'; g.beginPath(); g.ellipse(r() * W, r() * H, 60 + r() * 120, 40 + r() * 80, r() * 3, 0, 7); g.fill(); }
  g.lineCap = 'round';
  for (let i = 0; i < 5200; i++) { const x = r() * W, y = r() * H, L = 12 + r() * 26, a = -1.57 + (r() - 0.5) * 0.9; g.strokeStyle = cols[Math.floor(r() * cols.length)]; g.lineWidth = 1.5 + r() * 2; g.beginPath(); g.moveTo(x, y); g.lineTo(x + Math.cos(a) * L, y + Math.sin(a) * L); g.stroke(); }
}, rep); }

export function meadow(T, st, { flat = 45, amp = 26, size = 1600, seed = 1 } = {}) {
  const { THREE } = T;
  const heightAt = (x, z) => { const q = Math.min(1, Math.max(0, (Math.hypot(x, z) - flat) / (flat * 1.6))), e = q * q * (3 - 2 * q); return e * amp * (0.5 + 0.5 * Math.sin(x * 0.012 + seed) * Math.cos(z * 0.015 + seed * 1.7)) + e * amp * 0.35 * Math.sin(x * 0.037 + z * 0.021 + seed * 3); };
  const geo = new THREE.PlaneGeometry(size, size, 160, 160); geo.rotateX(-Math.PI / 2);
  const p = geo.attributes.position; for (let i = 0; i < p.count; i++) p.setY(i, heightAt(p.getX(i), p.getZ(i)));
  geo.computeVertexNormals();
  const m = new THREE.Mesh(geo, new THREE.MeshStandardMaterial({ map: grassTex(T, [size / 5, size / 5]), roughness: 1 })); m.receiveShadow = true; st.add(m);
  return heightAt;
}

// clumps of blades near the camera, so the foreground is not a flat texture
export function tufts(T, st, { count = 2600, radius = 26, z = 0, seed = 3, skip = null } = {}) {
  const { THREE } = T, r = rng(seed), greens = ['#5da346', '#79bf58', '#4c9140', '#8ccb66'];
  const geo = new THREE.ConeGeometry(0.02, 0.24, 3); geo.translate(0, 0.12, 0);
  const mesh = new THREE.InstancedMesh(geo, T.mat('#ffffff', { flat: true }), count), m4 = new THREE.Matrix4(), q = new THREE.Quaternion(), e = new THREE.Euler(), s = new THREE.Vector3(), pos = new THREE.Vector3(), c = new THREE.Color();
  for (let i = 0; i < count; i++) {
    let x, zz; do { const a = r() * 6.283, d = Math.sqrt(r()) * radius; x = Math.cos(a) * d; zz = z + Math.sin(a) * d; } while (skip && skip(x, zz));
    e.set((r() - 0.5) * 0.6, r() * 6.28, (r() - 0.5) * 0.6); q.setFromEuler(e); const k = 0.7 + r() * 0.9; s.set(k, k, k); pos.set(x, 0, zz); m4.compose(pos, q, s);
    mesh.setMatrixAt(i, m4); mesh.setColorAt(i, c.set(shade(greens[i % 4], (r() - 0.5) * 0.2)));
  }
  mesh.castShadow = false; mesh.receiveShadow = true; st.add(mesh);
}

export function dirtRoad(T, st, { x = 0, width = 7, z = -30, len = 140 } = {}) {
  const tex = T.canvasTex(512, 512, (g, W, H) => {
    const r = rng(9); g.fillStyle = '#a98b63'; g.fillRect(0, 0, W, H);
    for (let i = 0; i < 1400; i++) { g.fillStyle = ['#8f7450', '#bb9c72', '#9c8059', '#c9ac84'][i % 4]; g.beginPath(); g.ellipse(r() * W, r() * H, 2 + r() * 7, 1.5 + r() * 4, r() * 3, 0, 7); g.fill(); }
    g.fillStyle = 'rgba(70,52,34,.2)'; g.fillRect(W * 0.2, 0, W * 0.1, H); g.fillRect(W * 0.7, 0, W * 0.1, H);       // wheel ruts
  }, [1, len / 7]);
  const m = T.plane(width, len, new T.THREE.MeshStandardMaterial({ map: tex, roughness: 1 })); m.rotation.x = -Math.PI / 2; m.position.set(x, 0.03, z); st.add(m);
}
