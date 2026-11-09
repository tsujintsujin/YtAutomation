// sky/day.js — bright daylight: the stage (sun, sky, haze) and clouds. Every daylight world starts with dayStage().
import { rng } from '/engine/core.js';

export function dayStage(T, o = {}) {
  const { THREE } = T; T.getRenderer().toneMapping = THREE.NoToneMapping;     // keep the flat toon colours exact
  const st = T.stage({ mood: 'day', fov: 44, fog: [420, 3400], fogColor: '#c4dcf4', keyPos: [15, 46, 22], keyIntensity: 2.2, ambient: 1.7, ambientSky: '#dbe8ff', bloom: 0, shadowSize: 36, ...o });
  st.camera.near = 0.3; st.camera.far = 5000; st.camera.updateProjectionMatrix(); st.sun.shadow.camera.far = 160; st.sun.shadow.camera.updateProjectionMatrix();
  st.hemi.groundColor = new THREE.Color('#b9a78f');
  return st;
}

function cloudTex(T, seed) { return T.canvasTex(512, 256, (g, W, H) => {
  const r = rng(seed); g.clearRect(0, 0, W, H);
  for (let i = 0; i < 46; i++) { const u = r(), x = W * (0.12 + u * 0.76), hump = Math.sin(u * Math.PI), R = 12 + hump * (16 + r() * 22), y = H * 0.68 - hump * r() * H * 0.34 - R * 0.3, gr = g.createRadialGradient(x, y, 0, x, y, R); gr.addColorStop(0, 'rgba(255,255,255,.95)'); gr.addColorStop(0.72, 'rgba(255,255,255,.82)'); gr.addColorStop(1, 'rgba(255,255,255,0)'); g.fillStyle = gr; g.beginPath(); g.arc(x, y, R, 0, 7); g.fill(); }
}); }

const CLOUDS = [[-330, 210, -1500, 420, 1], [-130, 430, -1700, 520, 2], [330, 250, -1500, 460, 3], [-620, 500, -1800, 560, 4], [640, 520, -1700, 500, 5], [150, 610, -1800, 380, 6]];
// clouds(T, st, { list: [[x, y, z, width, seed], ...], seed })   Far away, in front of a camera looking toward -z.
export function clouds(T, st, { list = CLOUDS, seed = 0 } = {}) {
  const { THREE } = T;
  list.forEach(([x, y, z, w, s]) => { const sp = new THREE.Sprite(new THREE.SpriteMaterial({ map: cloudTex(T, s + seed), transparent: true, depthWrite: false, fog: false })); sp.position.set(x, y, z); sp.scale.set(w, w / 2, 1); st.add(sp); });
}
