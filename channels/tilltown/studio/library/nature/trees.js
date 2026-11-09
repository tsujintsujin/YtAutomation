// nature/trees.js — a leafy tree made of faceted clumps, a pine, and forest() to scatter them.
// tree(T, x, z, size, seed, clumps) and pine(T, x, z, size, seed): add the result to the stage.
import { rng, shade } from '/engine/core.js';

export function tree(T, x, z, s, seed, clumps = 34) {
  const { THREE } = T, g = new THREE.Group(), r = rng(seed), greens = ['#4f9a3f', '#5fae48', '#468c3a', '#6bb850'];
  g.add(T.cyl(0.16 * s, 0.26 * s, 3.4 * s, '#6a5340', 0, 1.7 * s, 0, 8));
  const geo = new THREE.IcosahedronGeometry(1, 1);
  for (let i = 0; i < clumps; i++) { const a = r() * 6.28, u = r(), d = Math.sqrt(u) * 2.1 * s, y = (3.5 + r() * 3.1) * s - d * 0.32, c = new THREE.Mesh(geo, T.mat(shade(greens[i % 4], (r() - 0.5) * 0.24), { flat: true })), q = (0.55 + r() * 0.5) * s; c.scale.set(q, q * 0.86, q); c.position.set(Math.cos(a) * d, y, Math.sin(a) * d); c.rotation.set(r() * 3, r() * 3, 0); c.castShadow = true; c.receiveShadow = true; g.add(c); }
  g.position.set(x, 0, z); return g;
}

export function pine(T, x, z, s, seed) {
  const { THREE } = T, g = new THREE.Group(), r = rng(seed), c = shade('#2f6b3f', (r() - 0.5) * 0.3);
  g.add(T.cyl(0.12 * s, 0.2 * s, 1.6 * s, '#5e4733', 0, 0.8 * s, 0, 7));
  [[2.1, 2.6, 2.2], [1.65, 2.3, 3.7], [1.15, 2, 5.1]].forEach(([rad, h, y]) => { const m = T.cone(rad * s, h * s, T.mat(c, { flat: true }), 0, y * s, 0, 8); m.rotation.y = r() * 3; g.add(m); });
  g.position.set(x, 0, z); return g;
}

// scatter trees on the land. heightAt: from meadow(). skip(x, z): keep an area clear. Far trees use fewer clumps.
export function forest(T, st, { heightAt = () => 0, seed = 4, inner = 18, outer = 340, pines = 150, broad = 26, skip = null } = {}) {
  const r = rng(seed), place = (make) => { for (let tries = 0; tries < 40; tries++) { const a = r() * 6.283, d = inner + Math.sqrt(r()) * (outer - inner), x = Math.cos(a) * d, z = Math.sin(a) * d - 30; if (skip && skip(x, z)) continue; const t = make(x, z, d); t.position.y = heightAt(x, z) - 0.05; st.add(t); return; } };
  for (let i = 0; i < pines; i++) place((x, z) => pine(T, x, z, 1.2 + r() * 1.1, i + seed));
  for (let i = 0; i < broad; i++) place((x, z, d) => tree(T, x, z, 1.1 + r() * 0.8, i + seed + 500, d < 70 ? 24 : 16));
}
