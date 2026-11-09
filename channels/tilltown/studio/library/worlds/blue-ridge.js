// worlds/blue-ridge.js — forested mountains: grass clearing at the origin, trees around it, rows of ridges behind.
// blueRidge(T, { weather: 'day'|'storm', seed, road, pond, stage }) returns { stage, heightAt }. Seen looking toward -z.
import { dayStage, clouds } from '/library/sky/day.js';
import { stormStage, stormClouds } from '/library/sky/storm.js';
import { meadow, tufts, dirtRoad } from '/library/ground/terrain.js';
import { ridges } from '/library/nature/mountains.js';
import { forest } from '/library/nature/trees.js';
import { pond as makePond } from '/library/nature/water.js';

export function blueRidge(T, o = {}) {
  const { weather = 'day', seed = 1, road = false, pond = false, inner = 18 } = o, stormy = weather === 'storm';
  const stage = stormy ? stormStage(T, { fov: 60, ...o.stage }) : dayStage(T, { fov: 60, ...o.stage });
  const heightAt = meadow(T, stage, { flat: road ? 70 : 45, amp: 7, seed });   // low, so the forest and ridges stay in view
  const onRoad = (x, z) => road && Math.abs(x) < 4.2, inPond = (x, z) => pond && Math.hypot(x, z + 9) < 10.4;
  tufts(T, stage, { z: -6, radius: 24, seed: seed + 2, skip: (x, z) => z > 0.8 || onRoad(x, z) || inPond(x, z) });
  if (road) dirtRoad(T, stage);
  if (pond) makePond(T, stage);
  ridges(T, stage, { weather, seed: seed + 1 });
  forest(T, stage, { heightAt, seed: seed + 3, inner, outer: 230, pines: 190, broad: 46, skip: (x, z) => (road && Math.abs(x) < 9) || z > 2 || inPond(x, z) });
  if (stormy) stormClouds(T, stage, { seed }); else clouds(T, stage, { seed });
  return { stage, heightAt };
}
