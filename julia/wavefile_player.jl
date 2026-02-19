# using SampledSignals, FileIO, PortAudio, WAV
using WAV

audio, sr = wavread("/Users/mej/Documents/UM_stuff/data_tool_v1/sample_audio/alto_flute_palindromes_41k.wav")

wavplay(audio)