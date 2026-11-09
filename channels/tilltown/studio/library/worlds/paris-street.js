// worlds/paris-street.js — a whole place, assembled from the other categories: a Paris street in daylight with the
// Eiffel Tower at the end. Returns the stage; the shot adds its own camera and characters.
// Built to be seen looking toward -z (down the street) or from above it. Behind z = +18 there is nothing.
// Options: seed (different facades, trees, clouds), cafeAt (left block with the café, -1 for none), tower (false to hide),
//          towerAt [x, z], stage (dayStage overrides, e.g. { fov: 30 }).
import { dayStage, clouds } from '/library/sky/day.js';
import { road, sidewalks, grass, avenue } from '/library/ground/ground.js';
import { haussmannRow, farSkyline, ROW_LENGTHS } from '/library/buildings/haussmann.js';
import { tree } from '/library/nature/trees.js';
import { lamp, morrisColumn, awning, cafeTables } from '/library/street-props/paris.js';
import { eiffel } from '/library/landmarks/eiffel.js';

export function parisStreet(T, o = {}) {
  const { seed = 0, cafeAt = 1, tower = true, towerAt = [14, -850] } = o;
  const street = 8.5, roadHalf = 6, z0 = 18;
  const st = dayStage(T, o.stage);
  road(T, st, { halfWidth: roadHalf }); sidewalks(T, st, { road: roadHalf, street }); grass(T, st); avenue(T, st);
  haussmannRow(T, st, { street, z0, cafeAt, seed });
  if (cafeAt >= 0) { const z = z0 - ROW_LENGTHS.slice(0, cafeAt).reduce((a, b) => a + b, 0) - ROW_LENGTHS[cafeAt] / 2 + 2; awning(T, st, { street, z }); cafeTables(T, st, { street, z }); }
  for (const [x, z] of [[-6.5, -17], [6.5, -13], [-6.5, -31], [6.5, -29], [-6.5, -45], [6.5, -44]]) st.add(tree(T, x, z, 1.05, Math.abs(z) + seed));
  for (const [x, z] of [[6.4, -14], [-6.4, -24], [6.4, -21], [-6.4, -38], [6.4, -37]]) lamp(T, st, x, z);
  morrisColumn(T, st, 7.2, -8);
  for (let z = -95, i = 0; z > -640; z -= 30, i++) st.add(tree(T, -7, z, 1.5, i + 40 + seed), tree(T, 27, z, 1.5, i + 90 + seed));
  if (tower) { const tw = eiffel(T); tw.position.set(towerAt[0], 0, towerAt[1]); st.add(tw); }
  farSkyline(T, st);
  clouds(T, st, { seed });
  return st;
}
