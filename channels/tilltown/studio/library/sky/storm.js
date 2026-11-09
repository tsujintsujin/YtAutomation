// sky/storm.js — a stormy but readable sky: dim blue light, low grey clouds.
import { clouds } from '/library/sky/day.js';

export function stormStage(T, o = {}) {
  const { THREE } = T; T.getRenderer().toneMapping = THREE.NoToneMapping;
  const st = T.stage({ mood: 'day', sky: ['#232c4d', '#3f4d7a', '#7d88a8'], fov: 44, fog: [300, 2600], fogColor: '#8390ad', keyPos: [-12, 40, 18], keyColor: '#dfe6ff', keyIntensity: 1.25, ambient: 1.85, ambientSky: '#b9c6e6', bloom: 0, shadowSize: 36, ...o });
  st.camera.near = 0.3; st.camera.far = 5000; st.camera.updateProjectionMatrix(); st.sun.shadow.camera.far = 160; st.sun.shadow.camera.updateProjectionMatrix();
  st.hemi.groundColor = new THREE.Color('#7f7a78');
  return st;
}

const STORM = [[-60, 70, -220, 260, 1], [90, 95, -260, 320, 2], [-20, 130, -330, 420, 3], [140, 60, -200, 220, 4], [-150, 110, -300, 360, 5], [30, 45, -180, 180, 6], [-90, 165, -380, 460, 7], [120, 170, -400, 500, 8]];
export function stormClouds(T, st, { seed = 0, color = '#3b4361' } = {}) { clouds(T, st, { list: STORM, seed, color }); }
