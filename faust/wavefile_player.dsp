import("stdfaust.lib");

declare filename "/Users/mej/Documents/UM_stuff/data_tool_v1/sample_audio/alto_flute_palindromes_41k.wav";

player = soundfile(filename);
process = player;

// vol = hslider("Volume[style:knob]", 1, 0, 2, 0.01);
// play = button("Play/Pause");

// player = soundfile(filename);
// process = vol * (play :> player);