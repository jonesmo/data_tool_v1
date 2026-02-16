import numpy as np
import modusa as ms
from IPython.display import display

import os
import timeit

cwd = os.getcwd()
audio_to_load = os.path.join(cwd, "sample_audio/alto_flute_palindromes_41k.wav")

def test_load_wav(test_audio):
	y, sr, title = ms.load.audio(test_audio)
	# assert title == "sample"
	assert y.size != 0
	assert y.ndim == 2
	assert sr == 44100
 
	return y, sr



if __name__ == "__main__":
  start_time = timeit.default_timer()
  y, sr = test_load_wav(audio_to_load)
  
  player = ms.play.audio(y, sr)
  print(player.data)
  
  end_time = timeit.default_timer()
  print("Execution time: ", end_time - start_time, " seconds")