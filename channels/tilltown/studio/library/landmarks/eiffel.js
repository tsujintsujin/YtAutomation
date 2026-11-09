// landmarks/eiffel.js — the Eiffel Tower, 1 unit = 1 metre, base centred at the origin. eiffel(T) returns a group to position.

function lattice(T, rep, col = '#86644a') { return T.canvasTex(256, 512, (g, W, H) => {
  g.clearRect(0, 0, W, H); g.strokeStyle = col; g.lineWidth = 18; g.strokeRect(0, 0, W, H); g.lineWidth = 11;
  g.beginPath(); g.moveTo(0, 0); g.lineTo(W, H); g.moveTo(W, 0); g.lineTo(0, H); g.stroke();
}, rep); }

export function eiffel(T) {
  const { THREE } = T, tower = new THREE.Group();
  const iron = T.mat('#7d5c40'), dark = T.mat('#5e4430');
  const latMat = (rep) => new THREE.MeshStandardMaterial({ map: lattice(T, rep), alphaTest: 0.4, side: THREE.DoubleSide, roughness: 1 });
  const R2 = Math.SQRT2;
  const frustum = (hwB, hwT, y0, y1, mat) => { const m = new THREE.Mesh(new THREE.CylinderGeometry(hwT * R2, hwB * R2, y1 - y0, 4, 1, true), mat); m.rotation.y = Math.PI / 4; m.position.set(0, (y0 + y1) / 2, 0); return m; };
  for (const sx of [-1, 1]) for (const sz of [-1, 1]) {           // the four legs, leaning in
    const a = new THREE.Vector3(sx * 50, 0, sz * 50), b = new THREE.Vector3(sx * 30, 60, sz * 30), mid = a.clone().add(b).multiplyScalar(0.5), dir = b.clone().sub(a), L = dir.length();
    const leg = new THREE.Mesh(new THREE.CylinderGeometry(9 * R2, 13 * R2, L, 4, 1, true), latMat([8, 5])); leg.position.copy(mid); leg.quaternion.setFromUnitVectors(new THREE.Vector3(0, 1, 0), dir.normalize()); leg.rotateY(Math.PI / 4); tower.add(leg);
    const core = new THREE.Mesh(new THREE.CylinderGeometry(4 * R2, 6 * R2, L, 4), dark); core.position.copy(mid); core.quaternion.copy(leg.quaternion); tower.add(core);
  }
  for (const z of [34, -34]) { const arch = new THREE.Mesh(new THREE.TorusGeometry(36, 1.6, 8, 40, Math.PI), iron); arch.position.set(0, 2, z); tower.add(arch); }
  for (const x of [34, -34]) { const arch = new THREE.Mesh(new THREE.TorusGeometry(36, 1.6, 8, 40, Math.PI), iron); arch.position.set(x, 2, 0); arch.rotation.y = Math.PI / 2; tower.add(arch); }
  tower.add(T.box(92, 7, 92, iron, 0, 60, 0));
  tower.add(frustum(36, 21, 63, 116, latMat([8, 4])), frustum(20, 12, 63, 116, dark));
  tower.add(T.box(50, 4.5, 50, iron, 0, 117.5, 0));
  tower.add(frustum(18, 4.5, 120, 276, latMat([8, 11])), frustum(9, 2.6, 120, 276, dark));
  tower.add(T.box(13, 8, 13, iron, 0, 280, 0), T.cyl(1, 1.8, 40, iron, 0, 304, 0, 8));
  return tower;
}
