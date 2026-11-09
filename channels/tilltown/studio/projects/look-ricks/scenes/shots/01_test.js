// 5-second look test (Ricks Clips look), now built from the shared library. Word times: "1925" 0.14, "sold" 2.24, "Eiffel Tower" 2.74-3.3.
import { registerShot, ease, prog, lerp } from '/engine/core.js';
import { parisStreet } from '/library/worlds/paris-street.js';
import { drawToon, toonCard } from '/library/characters/toon.js';
import { LUSTIG, PASSERSBY } from '/library/characters/cast.js';

const EXTRAS = [
  { x: 3.6, z: -8, facing: -1, expr: 'neutral', outfit: PASSERSBY[0] },
  { x: -4.6, z: -13, facing: 1, expr: 'happy', outfit: PASSERSBY[1] },
  { x: 4.9, z: -21, facing: -1, expr: 'neutral', outfit: PASSERSBY[2] },
];

registerShot('s001', {
  kind: '3d',
  init(T) {
    const st = parisStreet(T);
    const lustig = toonCard(T, st, -0.4, 2.0);
    const extras = EXTRAS.map((e) => toonCard(T, st, e.x, e.z, 480, 720, 2.4));
    return { stage: st, lustig, extras };
  },
  draw(s, t, info) {
    const k = ease.inOut(t / info.dur), cam = s.stage.camera;
    cam.position.set(lerp(2.1, 1.7, k), lerp(1.42, 1.5, k), lerp(8.6, 6.9, k)); cam.lookAt(-7, 7.6, -100);
    const sold = 2.24, up = ease.out(prog(t, sold - 0.14, sold + 0.2)) * (1 - ease.inOut(prog(t, 4.3, 4.85)));
    const pulse = 1 + 0.035 * Math.sin(Math.PI * prog(t, sold - 0.05, sold + 0.3));
    s.lustig.mesh.scale.set(pulse, pulse, 1);
    const expr = t < sold ? 'neutral' : t < 3.3 ? 'smirk' : 'smug';
    const look = t > sold && t < 3.3 ? [1, -0.5] : [0, 0];
    s.lustig.redraw((g, W, H) => drawToon(g, { x: W / 2 - 40, y: H - 30, s: 2.1, facing: 1, outfit: LUSTIG, expr, look, blink: (t % 3.4) > 3.27, bob: Math.sin(t * 2.3) * 1.6,
      arms: { front: [lerp(0.12, 1.92, up), lerp(-0.05, -0.08, up)], back: [-0.1, 0.05] } }));
    s.lustig.face(cam);
    s.extras.forEach((c, i) => { const e = EXTRAS[i]; c.redraw((g, W, H) => drawToon(g, { x: W / 2, y: H - 22, s: 1.58, facing: e.facing, outfit: e.outfit, expr: e.expr, bob: Math.sin(t * 2 + i * 2) * 1.5, blink: ((t + i) % 3.1) > 3.0 })); c.face(cam); });
  },
});
