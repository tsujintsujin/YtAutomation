// nature/trees.js — a leafy tree made of faceted clumps. tree(T, x, z, size, seed): add the result to the stage.
import { rng, shade } from '/engine/core.js';

export function tree(T, x, z, s, seed) {
  const { THREE } = T, g = new THREE.Group(), r = rng(seed), greens = ['#4f9a3f', '#5fae48', '#468c3a', '#6bb850'];
  g.add(T.cyl(0.16 * s, 0.26 * s, 3.4 * s, '#6a5340', 0, 1.7 * s, 0, 8));
  const geo = new THREE.IcosahedronGeometry(1, 1);
  for (let i = 0; i < 34; i++) { const a = r() * 6.28, u = r(), d = Math.sqrt(u) * 2.1 * s, y = (3.5 + r() * 3.1) * s - d * 0.32, c = new THREE.Mesh(geo, T.mat(shade(greens[i % 4], (r() - 0.5) * 0.24), { flat: true })), q = (0.55 + r() * 0.5) * s; c.scale.set(q, q * 0.86, q); c.position.set(Math.cos(a) * d, y, Math.sin(a) * d); c.rotation.set(r() * 3, r() * 3, 0); c.castShadow = true; c.receiveShadow = true; g.add(c); }
  g.position.set(x, 0, z); return g;
}
