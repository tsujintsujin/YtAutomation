// street-props/paris.js — street lamp, Morris advertising column, café awning, café tables.

export function lamp(T, st, x, z) {
  const c = '#2c463a'; st.add(T.cyl(0.06, 0.1, 3.8, c, x, 1.9, z, 8), T.cyl(0.16, 0.2, 0.3, c, x, 0.15, z, 8), T.box(0.34, 0.5, 0.34, '#fff2c8', x, 4.05, z), T.cone(0.32, 0.26, c, x, 4.43, z, 4));
}

export function morrisColumn(T, st, x, z) {
  const posters = T.canvasTex(512, 256, (g, W, H) => { g.fillStyle = '#3b6b52'; g.fillRect(0, 0, W, H); [['#e8c65a', 20], ['#c9503e', 150], ['#f0e6d2', 280], ['#5d86b8', 400]].forEach(([c, px]) => { g.fillStyle = c; g.fillRect(px, 30, 96, 190); g.fillStyle = 'rgba(40,30,30,.55)'; g.fillRect(px + 12, 52, 72, 12); g.fillRect(px + 12, 76, 56, 9); g.fillRect(px + 12, 150, 72, 40); }); });
  st.add(T.cyl(0.66, 0.66, 3.1, new T.THREE.MeshStandardMaterial({ map: posters, roughness: 1 }), x, 1.71, z, 24), T.sphere(0.72, T.mat('#2f5442'), x, 3.32, z));
}

// striped awning on the wall at x = side * street (side -1 = left wall, 1 = right wall), centred at z
export function awning(T, st, { side = -1, street = 8.5, z = -8, len = 12 } = {}) {
  const { THREE } = T, out = -side;
  const stripes = T.canvasTex(64, 128, (g, W, H) => { g.fillStyle = '#c23b2e'; g.fillRect(0, 0, W, H / 2); g.fillStyle = '#f4ead6'; g.fillRect(0, H / 2, W, H / 2); }, [1, 8]);
  const aw = T.box(2.7, 0.1, len, new THREE.MeshStandardMaterial({ map: stripes, roughness: 1 }), side * street + out * 1.1, 3.95, z); aw.rotation.z = side * 0.62; st.add(aw);
  const valance = T.canvasTex(256, 64, (g, W, H) => { for (let i = 0; i < 8; i++) { g.fillStyle = i % 2 ? '#f4ead6' : '#c23b2e'; g.fillRect(i * W / 8, 0, W / 8, H); } }, [8, 1]);
  st.add(T.box(0.05, 0.42, len, new THREE.MeshStandardMaterial({ map: valance, roughness: 1 }), side * street + out * 2.18, 3.0, z));
}

export function cafeTables(T, st, { side = -1, street = 8.5, z = -8 } = {}) {
  const x = side * street - side * 1.3;
  for (const tz of [z + 4.5, z + 0.5, z - 3.5]) st.add(T.cyl(0.38, 0.38, 0.05, '#2f3a34', x, 0.92, tz, 18), T.cyl(0.04, 0.05, 0.76, '#2f3a34', x, 0.52, tz, 8));
}
