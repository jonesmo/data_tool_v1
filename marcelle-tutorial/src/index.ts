import '@marcellejs/core/dist/marcelle.css';
import * as marcelle from '@marcellejs/core';
import { waveformComponent } from './components/waveform';

// GUI stuff
// const input = marcelle.sketchPad();

// const myDashboard = marcelle.dashboard({
//   title: 'My First Tutorial',
//   author: 'Myself',
// });

// myDashboard.page('Data Management').sidebar(input);

// // extract features from sketches
// const featureExtractor = marcelle.mobileNet();

// const label = marcelle.textInput();
// label.title = 'Instance label';

// myDashboard.page('Data Management').sidebar(input, featureExtractor).use(label);

// label.$value.subscribe((currentInput) => {
//   console.log('currentInput:', currentInput);
// });

// const $instances = input.$images
//   .map(async (img) => ({
//     x: await featureExtractor.process(img),
//     y: label.$value.get(),
//     thumbnail: input.$thumbnails.get(),
//   }))
//   .awaitPromises();

// // show the dashboard
// myDashboard.show();

// const waveform = marcelle.waveform();

const audioUrl = 'https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3';
const waveform: any = waveformComponent(audioUrl);

const myDashboard = marcelle.dashboard({
  title: 'Audio Waveform Display',
  author: 'Your Name',
});

// Display waveform in dashboard
myDashboard.page('Waveform').use(waveform);

myDashboard.show();
