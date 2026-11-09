// One view per library category, plus reuse tests. Re-render when the library grows:
//   studio.cmd node render.mjs --project projects\library-preview --sheet --gl gpu --format jpeg
import { E, registerShot, FONTS, text, backdrop, mood } from '/engine/core.js';
import { parisStreet } from '/library/worlds/paris-street.js';
import { dayStage, clouds } from '/library/sky/day.js';
import { road, sidewalks, grass, avenue } from '/library/ground/ground.js';
import { haussmannRow } from '/library/buildings/haussmann.js';
import { tree } from '/library/nature/trees.js';
import { lamp, morrisColumn, awning, cafeTables } from '/library/street-props/paris.js';
import { eiffel } from '/library/landmarks/eiffel.js';
import { drawToon, toonCard, EXPR } from '/library/characters/toon.js';
import { LUSTIG, PASSERSBY } from '/library/characters/cast.js';

const label = (g, s) => text(g, s, 44, 64, { size: 46, font: FONTS.ui, weight: 900, align: 'left', stroke: 10, strokeColor: 'rgba(0,0,0,.85)' });
function view(id, name, build, pos, look) {
  registerShot(id, { kind: '3d', init(T) { return { stage: build(T) }; }, draw(s) { s.stage.camera.position.set(...pos); s.stage.camera.lookAt(...look); }, overlay(g) { label(g, name); } });
}

view('s001', 'WORLDS: paris-street', (T) => parisStreet(T), [1.9, 1.46, 7.7], [-7, 7.6, -100]);
view('s002', 'REUSE: same world, new seed, café moved, from above', (T) => parisStreet(T, { seed: 21, cafeAt: 3 }), [0, 30, 14], [6, 8, -120]);
view('s003', 'REUSE: same world, at the café', (T) => { const st = parisStreet(T); const c = toonCard(T, st, -5, -3.6); c.redraw((g, W, H) => drawToon(g, { x: W / 2, y: H - 30, s: 2.1, facing: -1, outfit: LUSTIG, expr: 'smug' })); c.mesh.rotation.y = 0.5; return st; }, [-2.2, 1.55, 3], [-8.5, 2.5, -14]);
view('s004', 'LANDMARKS: eiffel', (T) => { const st = dayStage(T); grass(T, st, { zStart: 1000 }); st.add(eiffel(T)); clouds(T, st); return st; }, [220, 40, 460], [0, 150, 0]);
view('s005', 'BUILDINGS: haussmann row', (T) => { const st = dayStage(T); road(T, st); sidewalks(T, st); grass(T, st); haussmannRow(T, st); return st; }, [5, 7, 22], [-8.5, 10, -25]);
view('s006', 'NATURE: trees', (T) => { const st = dayStage(T); grass(T, st, { zStart: 60 }); [[-12, 1, 1], [-6, 1.25, 2], [0, 0.9, 3], [6, 1.35, 4], [12, 1, 5]].forEach(([x, s, seed]) => st.add(tree(T, x, 0, s, seed))); clouds(T, st); return st; }, [0, 2.6, 26], [0, 5, 0]);
view('s007', 'STREET PROPS: awnings, tables, lamps, column', (T) => { const st = dayStage(T); road(T, st); sidewalks(T, st); grass(T, st); haussmannRow(T, st, { lengths: [24, 24, 24], z0: 12, cafeAt: 0 }); for (const side of [-1, 1]) { awning(T, st, { side, z: 0 }); cafeTables(T, st, { side, z: 0 }); lamp(T, st, side * 6.4, -7); } morrisColumn(T, st, 7.2, 7); return st; }, [0, 2, 19], [0, 3.2, -10]);
view('s008', 'GROUND: cobbles, sidewalks, avenue, grass', (T) => { const st = dayStage(T, { fov: 30 }); road(T, st); sidewalks(T, st); grass(T, st); avenue(T, st); return st; }, [0, 2.4, 26], [2, 1, -60]);
registerShot('s009', { draw(g) {
  backdrop(g, mood('day').sky); g.fillStyle = '#b89c7c'; g.fillRect(0, 860, E.W, 220);
  Object.keys(EXPR).forEach((e, i) => drawToon(g, { x: 150 + i * 270, y: 960, s: 1.7, facing: 1, outfit: i % 2 ? PASSERSBY[(i >> 1) % 3] : LUSTIG, expr: e }));
  label(g, 'CHARACTERS: toon + every expression');
} });
