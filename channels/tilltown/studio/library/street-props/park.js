// street-props/park.js — a carved wooden park sign. woodSign(T, ['LINE ONE', 'LINE TWO']) returns a group facing +z.
export function woodSign(T, lines = ['SIGN']) {
  const { THREE } = T, g = new THREE.Group();
  const tex = T.canvasTex(768, 384, (c, W, H) => { c.fillStyle = '#6a4a30'; c.fillRect(0, 0, W, H); c.fillStyle = 'rgba(40,24,12,.28)'; for (let i = 0; i < 7; i++) c.fillRect(0, (i * H) / 7, W, 4); c.strokeStyle = '#e8d7a8'; c.lineWidth = 8; c.strokeRect(14, 14, W - 28, H - 28); c.fillStyle = '#f4e6bd'; c.textAlign = 'center'; c.textBaseline = 'middle'; c.font = '700 72px Fredoka'; lines.forEach((s, i) => c.fillText(s, W / 2, H / 2 + (i - (lines.length - 1) / 2) * 92)); });
  g.add(T.box(2.3, 1.15, 0.1, new THREE.MeshStandardMaterial({ map: tex, roughness: 1 }), 0, 1.65, 0));
  for (const x of [-1, 1]) g.add(T.cyl(0.08, 0.1, 2.4, '#5a3f2a', x, 1.2, -0.08, 8));
  return g;
}
