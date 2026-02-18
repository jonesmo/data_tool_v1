import WaveSurfer from 'wavesurfer.js';
import { html } from '@marcellejs/core';

// This function creates the component
// export function waveformComponent(audioLocator: string) {
//   let wavesurfer: WaveSurfer = null;
//   const container = html`<div style="width:100%; height:128px;"></div>`;

//   // Initialize WaveSurfer when the audioLocator is available
//   function init() {
//     if (wavesurfer) {
//       wavesurfer.destroy();
//     }
//     wavesurfer = WaveSurfer.create({
//       container: container,
//       waveColor: 'violet',
//       progressColor: 'purple',
//       height: 128,
//     });
//     wavesurfer.load(audioLocator);
//   }

//   // If audioLocator changes, re-initialize
//   if (audioLocator) {
//     init();
//   }

//   // Marcelle component format - expose container
//   return {
//     $el: container,
//   };
// }

export function waveformComponent(audioUrl) {
  const container = document.createElement('div'); // Standard DOM element
  container.style.width = '100%';
  container.style.height = '128px';

  // Setup WaveSurfer
  const wavesurfer: WaveSurfer = WaveSurfer.create({
    container: container,
    waveColor: 'violet',
    progressColor: 'purple',
    height: 128,
  });
  wavesurfer.load(audioUrl);

  // Marcelle-compatible component: return $el property
  return {
    $el: container,
    destroy() {
      wavesurfer && wavesurfer.destroy();
    },
  };
}
