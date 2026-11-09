// vehicles/truck.js — a 1960s pickup, about 5 m long along x, front toward +x. pickup(T, { color }) returns a group.
export function pickup(T, { color = '#3f6b4c' } = {}) {
  const { THREE } = T, g = new THREE.Group(), paint = T.mat(color), dark = T.mat('#26242b'), chrome = T.mat('#d8dde2', { roughness: 0.3, metalness: 0.4 });
  g.add(T.box(1.75, 0.55, 1.9, paint, 1.55, 0.98, 0), T.box(1.55, 1.2, 1.9, paint, 0.1, 1.2, 0), T.box(2.2, 0.75, 1.9, paint, -1.85, 0.98, 0), T.box(2.05, 0.1, 1.72, dark, -1.85, 1.37, 0));
  const glass = T.mat('#8fbad8', { roughness: 0.25 });
  g.add(T.box(0.06, 0.56, 1.66, glass, 0.89, 1.52, 0)); for (const s of [-1, 1]) g.add(T.box(0.98, 0.56, 0.06, glass, 0.15, 1.52, s * 0.96));
  g.add(T.box(0.14, 0.2, 2.02, chrome, 2.45, 0.68, 0), T.box(0.1, 0.2, 2.02, chrome, -2.98, 0.68, 0), T.box(0.05, 0.4, 1.3, chrome, 2.43, 1.05, 0));
  for (const s of [-1, 1]) g.add(T.sphere(0.13, T.mat('#fff4c8', { roughness: 0.3 }), 2.43, 1.1, s * 0.74));
  for (const x of [1.6, -1.75]) for (const s of [-1, 1]) { const w = T.cyl(0.42, 0.42, 0.3, dark, x, 0.42, s * 0.92, 20); w.rotation.x = Math.PI / 2; g.add(w); const h = T.cyl(0.2, 0.2, 0.32, chrome, x, 0.42, s * 0.92, 14); h.rotation.x = Math.PI / 2; g.add(h); }
  return g;
}
