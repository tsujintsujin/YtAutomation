// nature/mountains.js — rows of rounded, tree-covered ridges fading into the distance. Seen looking toward -z.
const LAYERS = [[-760, 95], [-1150, 175], [-1650, 280], [-2350, 430]];
const COLORS = { day: ['#3f7d44', '#5b9460', '#86b08c', '#afcbc4'], storm: ['#27523a', '#38654e', '#55806d', '#7a9a90'] };

export function ridges(T, st, { weather = 'day', seed = 2 } = {}) {
  const { THREE } = T;
  LAYERS.forEach(([z, h], i) => {
    const sh = new THREE.Shape(), a = seed + i * 1.7; sh.moveTo(-5000, -80);
    for (let x = -5000; x <= 5000; x += 10) sh.lineTo(x, h * (0.68 + 0.2 * Math.sin(x * 0.0021 + a) + 0.12 * Math.sin(x * 0.0057 + a * 2)) + (i < 2 ? 3 * Math.sin(x * 0.09 + a) + 2 * Math.sin(x * 0.23 + a) : 0));
    sh.lineTo(5000, -80); sh.closePath();
    const m = new THREE.Mesh(new THREE.ShapeGeometry(sh), new THREE.MeshBasicMaterial({ color: new THREE.Color(COLORS[weather][i]), fog: false })); m.position.z = z; st.add(m);
  });
}
