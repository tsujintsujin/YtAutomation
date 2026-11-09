// characters/toon.js — Tilltown characters in the Ricks Clips look (art reference, Justin 2026-11-08):
// flat 2D cut-outs with a dark outline, a big round white head, strong simple faces, a hat that tells the role,
// a small clothed torso, thin dark stick arms and legs, small white round hands.
// Local space: feet on y = 0, up is -y, the figure faces +x when facing = 1. Height ≈ 310 units without a hat.

export const LINE = '#1d1a22';

// expressions: brows [front, back] as [lift of inner end, lift of outer end] in head radii; eyes; mouth
export const EXPR = {
  neutral: { brows: [[0, 0], [0, 0]], eyes: 'dot', mouth: 'line' },
  smug:    { brows: [[0.05, 0.12], [-0.02, 0.0]], eyes: 'lid', mouth: 'smirk' },
  smirk:   { brows: [[0.02, 0.08], [0, 0.02]], eyes: 'dot', mouth: 'smirk' },
  angry:   { brows: [[-0.1, 0.06], [-0.1, 0.06]], eyes: 'dot', mouth: 'frown' },
  worried: { brows: [[0.1, -0.04], [0.1, -0.04]], eyes: 'dot', mouth: 'wavy' },
  shocked: { brows: [[0.14, 0.14], [0.14, 0.14]], eyes: 'wide', mouth: 'o' },
  happy:   { brows: [[0.06, 0.06], [0.06, 0.06]], eyes: 'dot', mouth: 'smile' },
  ouch:    { brows: [[-0.1, 0.06], [-0.1, 0.06]], eyes: 'x', mouth: 'o' },
};

const lerp = (a, b, k) => a + (b - a) * k;
function outlined(g, path, fill, lw) { path(); if (fill) { g.fillStyle = fill; g.fill(); } g.lineWidth = lw; g.strokeStyle = LINE; g.lineJoin = 'round'; g.lineCap = 'round'; g.stroke(); }
function line(g, pts, w, col = LINE) { g.beginPath(); g.moveTo(...pts[0]); for (const p of pts.slice(1)) g.lineTo(...p); g.lineWidth = w; g.strokeStyle = col; g.lineCap = 'round'; g.lineJoin = 'round'; g.stroke(); }

// arm: from shoulder, angles in radians measured from straight down, positive = toward the facing side
function arm(g, sx, sy, a1, a2, hand) {
  const L1 = 44, L2 = 42;
  const ex = sx + Math.sin(a1) * L1, ey = sy + Math.cos(a1) * L1;
  const hx = ex + Math.sin(a1 + a2) * L2, hy = ey + Math.cos(a1 + a2) * L2;
  line(g, [[sx, sy], [ex, ey], [hx, hy]], 4.6);
  outlined(g, () => { g.beginPath(); g.arc(hx, hy, 8.5, 0, Math.PI * 2); }, hand, 2.8);
  return [hx, hy];
}

function hat(g, h, r, lw) {
  const c = h.color || '#3a3640', band = h.band || LINE;
  if (h.type === 'fedora') {
    // brim (back half), crown with a centre pinch, band, brim front edge
    const by = -r * 0.68;
    outlined(g, () => { g.beginPath(); g.ellipse(r * 0.04, by, r * 1.12, r * 0.19, -0.06, 0, Math.PI * 2); }, c, lw);
    outlined(g, () => {
      g.beginPath(); g.moveTo(-r * 0.68, by); g.bezierCurveTo(-r * 0.72, by - r * 0.56, -r * 0.42, by - r * 0.72, -r * 0.1, by - r * 0.62);
      g.quadraticCurveTo(r * 0.05, by - r * 0.55, r * 0.2, by - r * 0.64); g.bezierCurveTo(r * 0.5, by - r * 0.74, r * 0.8, by - r * 0.54, r * 0.76, by);
      g.quadraticCurveTo(r * 0.04, by + r * 0.12, -r * 0.68, by); g.closePath();
    }, c, lw);
    outlined(g, () => { g.beginPath(); g.moveTo(-r * 0.69, by - r * 0.06); g.quadraticCurveTo(r * 0.04, by + r * 0.05, r * 0.77, by - r * 0.06); g.lineTo(r * 0.76, by - r * 0.2); g.quadraticCurveTo(r * 0.04, by - r * 0.09, -r * 0.7, by - r * 0.2); g.closePath(); }, band, lw * 0.8);
    g.globalAlpha = 0.35; line(g, [[-r * 0.42, by - r * 0.5], [-r * 0.24, by - r * 0.57]], r * 0.06, '#ffffff'); g.globalAlpha = 1;   // sheen
  }
  if (h.type === 'campaign') {        // ranger's flat-brimmed hat with a pinched top
    const by = -r * 0.64;
    outlined(g, () => { g.beginPath(); g.ellipse(r * 0.02, by, r * 1.46, r * 0.2, -0.03, 0, Math.PI * 2); }, c, lw);
    outlined(g, () => { g.beginPath(); g.moveTo(-r * 0.6, by); g.bezierCurveTo(-r * 0.62, by - r * 0.5, -r * 0.42, by - r * 0.92, -r * 0.16, by - r * 0.94); g.quadraticCurveTo(0, by - r * 0.76, r * 0.16, by - r * 0.94); g.bezierCurveTo(r * 0.42, by - r * 0.92, r * 0.62, by - r * 0.5, r * 0.6, by); g.quadraticCurveTo(0, by + r * 0.1, -r * 0.6, by); g.closePath(); }, c, lw);
    outlined(g, () => { g.beginPath(); g.moveTo(-r * 0.6, by - r * 0.04); g.quadraticCurveTo(0, by + r * 0.08, r * 0.6, by - r * 0.04); g.lineTo(r * 0.58, by - r * 0.18); g.quadraticCurveTo(0, by - r * 0.06, -r * 0.58, by - r * 0.18); g.closePath(); }, band, lw * 0.8);
    line(g, [[-r * 0.24, by - r * 0.72], [-r * 0.12, by - r * 0.46]], r * 0.05, 'rgba(40,28,14,.55)'); line(g, [[r * 0.24, by - r * 0.72], [r * 0.12, by - r * 0.46]], r * 0.05, 'rgba(40,28,14,.55)');
  }
}

function face(g, fx, r, ex, o) {
  const eyeY = -r * 0.02, ed = r * 0.31, look = o.look || [0, 0];
  const eyes = [fx + ed * 0.95, fx - ed * 1.0];        // front eye, back eye
  eyes.forEach((x, i) => {
    const lx = x + look[0] * r * 0.05, ly = eyeY + look[1] * r * 0.05;
    if (o.blink) { line(g, [[x - r * 0.08, eyeY], [x + r * 0.08, eyeY]], r * 0.06); return; }
    if (ex.eyes === 'x') { const q = r * 0.1; line(g, [[x - q, eyeY - q], [x + q, eyeY + q]], r * 0.06); line(g, [[x + q, eyeY - q], [x - q, eyeY + q]], r * 0.06); return; }
    if (ex.eyes === 'wide') { outlined(g, () => { g.beginPath(); g.ellipse(x, eyeY, r * 0.13, r * 0.15, 0, 0, Math.PI * 2); }, '#ffffff', r * 0.045); g.fillStyle = LINE; g.beginPath(); g.arc(lx, ly, r * 0.055, 0, Math.PI * 2); g.fill(); return; }
    g.fillStyle = LINE; g.beginPath(); g.ellipse(lx, ly, r * 0.075, r * 0.105, 0, 0, Math.PI * 2); g.fill();
    if (ex.eyes === 'lid') { g.fillStyle = o.headColor; g.fillRect(x - r * 0.12, eyeY - r * 0.16, r * 0.24, r * 0.15); line(g, [[x - r * 0.11, eyeY - r * 0.01], [x + r * 0.11, eyeY - r * 0.03]], r * 0.055); }
  });
  if (!o.noBrows) ex.brows.forEach(([inner, outer], i) => {           // i = 0 front brow, 1 back brow; inner end is toward the nose
    const x = eyes[i], dir = i === 0 ? 1 : -1, by = eyeY - r * 0.26;
    line(g, [[x - dir * r * 0.16, by - inner * r], [x + dir * r * 0.18, by - outer * r]], r * 0.1);
  });
  const mx = fx + r * 0.02, my = r * 0.36;
  switch (o.talk > 0.05 ? 'talk' : ex.mouth) {
    case 'line': line(g, [[mx - r * 0.12, my], [mx + r * 0.12, my]], r * 0.055); break;
    case 'smirk': g.beginPath(); g.moveTo(mx - r * 0.14, my + r * 0.02); g.quadraticCurveTo(mx + r * 0.06, my + r * 0.06, mx + r * 0.2, my - r * 0.07); g.lineWidth = r * 0.055; g.strokeStyle = LINE; g.lineCap = 'round'; g.stroke(); break;
    case 'frown': g.beginPath(); g.arc(mx, my + r * 0.12, r * 0.13, Math.PI * 1.2, Math.PI * 1.8); g.lineWidth = r * 0.055; g.strokeStyle = LINE; g.stroke(); break;
    case 'smile': g.beginPath(); g.arc(mx, my - r * 0.08, r * 0.15, Math.PI * 0.2, Math.PI * 0.8); g.lineWidth = r * 0.055; g.strokeStyle = LINE; g.stroke(); break;
    case 'wavy': g.beginPath(); for (let k = 0; k <= 12; k++) { const u = k / 12; g.lineTo(mx - r * 0.14 + u * r * 0.28, my + Math.sin(u * Math.PI * 2) * r * 0.035); } g.lineWidth = r * 0.05; g.strokeStyle = LINE; g.stroke(); break;
    case 'o': outlined(g, () => { g.beginPath(); g.ellipse(mx, my + r * 0.02, r * 0.07, r * 0.1, 0, 0, Math.PI * 2); }, '#5a2a2a', r * 0.045); break;
    case 'talk': outlined(g, () => { g.beginPath(); g.ellipse(mx, my, r * 0.1, r * (0.03 + 0.08 * o.talk), 0, 0, Math.PI * 2); }, '#5a2a2a', r * 0.045); break;
  }
}

// drawToon(g, { x, y, s, facing, outfit, expr, look, blink, talk, arms: { front: [a1, a2], back: [a1, a2] }, bob, tilt, noBrows, hatOff, prop })
// prop(g, handFront, handBack) draws something in the figure's own coordinates, after the front arm.
export function drawToon(g, o) {
  const of = o.outfit, f = o.facing ?? 1, ex = EXPR[o.expr] || EXPR.neutral;
  const r = 60, headY = -250 + (o.bob || 0), lw = 3.4;
  if (o.hatOnly) { g.save(); g.translate(o.x, o.y); g.scale((o.s ?? 1) * f, o.s ?? 1); g.translate(0, headY); if (of.hat) hat(g, of.hat, r, lw); g.restore(); return; }
  const af = o.arms?.front || [0.12, -0.05], ab = o.arms?.back || [-0.1, 0.05];
  g.save(); g.translate(o.x, o.y); if (o.tilt) g.rotate(o.tilt); g.scale((o.s ?? 1) * f, o.s ?? 1);
  // back arm, legs + shoes
  const handB = arm(g, -24, -184, ab[0], ab[1], of.hand || '#ffffff');
  for (const [hx, fx] of [[-11, -15], [11, 13]]) {
    line(g, [[hx, -108], [fx, -6]], 5);
    outlined(g, () => { g.beginPath(); g.ellipse(fx + 7, -5, 13, 6.5, 0, 0, Math.PI * 2); }, of.shoes || LINE, 2.5);
  }
  // torso (the clothes)
  const body = of.body || {};
  outlined(g, () => { g.beginPath(); g.moveTo(0, -206); g.bezierCurveTo(26, -206, 35, -160, 36, -118); g.quadraticCurveTo(36, -100, 20, -100); g.lineTo(-20, -100); g.quadraticCurveTo(-36, -100, -36, -118); g.bezierCurveTo(-35, -160, -26, -206, 0, -206); g.closePath(); }, body.color || '#3a3640', lw);
  if (body.type === 'suit') {
    outlined(g, () => { g.beginPath(); g.moveTo(-13, -199); g.lineTo(13, -199); g.lineTo(2, -150); g.closePath(); }, body.shirt || '#ffffff', 3);
    outlined(g, () => { g.beginPath(); g.moveTo(2, -194); g.lineTo(8, -186); g.lineTo(4, -158); g.lineTo(2, -152); g.lineTo(-1, -158); g.lineTo(-3, -186); g.closePath(); }, body.tie || '#d64a33', 2.5);
    line(g, [[-13, -199], [-4, -168], [2, -150]], 3); line(g, [[13, -199], [8, -172], [2, -150]], 3);       // lapels
    for (const by of [-138, -120]) { g.fillStyle = LINE; g.beginPath(); g.arc(8, by, 3.2, 0, Math.PI * 2); g.fill(); }
  }
  if (body.type === 'uniform') {
    outlined(g, () => { g.beginPath(); g.moveTo(-14, -200); g.lineTo(2, -176); g.lineTo(18, -200); g.lineTo(16, -180); g.lineTo(2, -166); g.lineTo(-12, -180); g.closePath(); }, body.collar || '#e9e0c6', 2.6);
    line(g, [[2, -166], [2, -116]], 2.6);
    outlined(g, () => { g.beginPath(); g.rect(-36, -120, 72, 13); }, body.belt || '#5a3f2a', 2.6);
    outlined(g, () => { g.beginPath(); g.rect(-5, -122, 14, 17); }, '#e8c65a', 2.2);
    g.fillStyle = '#ffd34d'; g.strokeStyle = LINE; g.lineWidth = 2; g.beginPath(); for (let k = 0; k < 10; k++) { const q = k % 2 ? 4.6 : 10, a = (k * Math.PI) / 5 - 1.57; g.lineTo(17 + Math.cos(a) * q, -158 + Math.sin(a) * q); } g.closePath(); g.fill(); g.stroke();
  }
  // front arm
  const handF = o.hideFront ? [22, -184] : arm(g, 22, -184, af[0], af[1], of.hand || '#ffffff');
  if (o.prop) o.prop(g, handF, handB);
  // head, hair patch (back side), face, hat
  g.save(); g.translate(0, headY);
  const headColor = of.head || '#ffffff';
  outlined(g, () => { g.beginPath(); g.arc(0, 0, r, 0, Math.PI * 2); }, headColor, 3.8);
  if (of.hair) { g.save(); g.beginPath(); g.arc(0, 0, r - 3, 0, Math.PI * 2); g.clip(); outlined(g, () => { g.beginPath(); g.ellipse(-r * 0.92, -r * 0.12, r * 0.3, r * 0.42, 0.15, 0, Math.PI * 2); }, of.hair, 3); g.restore(); }
  if (of.hairTop && (!of.hat || o.hatOff)) { g.save(); g.beginPath(); g.arc(0, 0, r - 2, 0, Math.PI * 2); g.clip(); outlined(g, () => { g.beginPath(); g.ellipse(-r * 0.05, -r * 0.82, r * 1.02, r * 0.5, -0.05, 0, Math.PI * 2); }, of.hairTop, 3); g.restore(); }
  face(g, r * 0.07, r, ex, { ...o, headColor });
  if (of.hat && !o.hatOff) hat(g, of.hat, r, lw);
  g.restore();
  g.restore();
}

// a flat toon cut-out standing in the 3D world: casts a real shadow, turns to face the camera. toonCard(T, st, x, z);
// each frame call .redraw((g, W, H) => drawToon(g, { x: W / 2, y: H - 30, s: 2.1, ... })) and .face(camera).
export function toonCard(T, st, x, z, W = 640, H = 960, hM = 2.4) {
  const { THREE } = T, c = document.createElement('canvas'); c.width = W; c.height = H; const g = c.getContext('2d');
  const tex = new THREE.CanvasTexture(c); tex.colorSpace = THREE.SRGBColorSpace; tex.anisotropy = 8;
  const mat = new THREE.MeshBasicMaterial({ map: tex, transparent: true, alphaTest: 0.04, side: THREE.DoubleSide, fog: false });
  const m = new THREE.Mesh(new THREE.PlaneGeometry(hM * W / H, hM), mat); m.castShadow = true;
  m.customDepthMaterial = new THREE.MeshDepthMaterial({ depthPacking: THREE.RGBADepthPacking, map: tex, alphaTest: 0.5, side: THREE.DoubleSide });
  m.position.set(x, hM / 2 - 0.075, z); st.add(m);
  return { mesh: m, face(cam) { m.rotation.y = Math.atan2(cam.position.x - m.position.x, cam.position.z - m.position.z); }, redraw(fn) { g.clearRect(0, 0, W, H); fn(g, W, H); tex.needsUpdate = true; } };
}
