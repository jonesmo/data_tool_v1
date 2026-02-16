import sys
import numpy as np
from scipy.io import wavfile
import sounddevice as sd
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton
from PySide6.QtCore import QTimer
import pyqtgraph as pg

# ----- Audio load -----
sample_rate, data = wavfile.read("/Users/mej/Documents/atlantic_center/alto_flute_palindromes.wav")

if data.dtype == np.int16:
    data = data.astype(np.float32) / 32768.0
elif data.dtype == np.int32:
    data = data.astype(np.float32) / 2147483648.0
elif np.issubdtype(data.dtype, np.floating):
    data = data.astype(np.float32)
else:
    raise RuntimeError("Unknown data type!")

if data.ndim == 1:
    data = np.column_stack((data, data))

left_channel = data[:, 0]
right_channel = data[:, 1]

# ----- GUI -----
class MainWindow(QMainWindow):
    def __init__(self, left, right, audio_data, sample_rate):
        super().__init__()
        self.sample_rate = sample_rate
        self.left = left
        self.right = right
        self.audio_data = audio_data
        self.length = len(left)
        self.position = 0

        self.setWindowTitle("Stereo Waveform with Playback Cursor (sounddevice + scipy)")
        central = QWidget()
        layout = QVBoxLayout(central)

        self.left_plot = pg.PlotWidget(title="Left Channel")
        self.right_plot = pg.PlotWidget(title="Right Channel")
        self.right_plot.setXLink(self.left_plot)

        self.left_curve = self.left_plot.plot(np.arange(len(left)), left, pen=pg.mkPen("b"))
        self.right_curve = self.right_plot.plot(np.arange(len(right)), right, pen=pg.mkPen("r"))

        self.cursor_left = self.left_plot.addLine(x=0, pen=pg.mkPen('g', width=2))
        self.cursor_right = self.right_plot.addLine(x=0, pen=pg.mkPen('g', width=2))

        layout.addWidget(self.left_plot)
        layout.addWidget(self.right_plot)
        self.play_button = QPushButton("Play")
        self.play_button.clicked.connect(self.start_playback)
        layout.addWidget(self.play_button)

        self.setCentralWidget(central)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_cursor)
        self.stream = None

    def start_playback(self):
        self.position = 0
        self.timer.start(1000 // 60)
        self.stream = sd.OutputStream(samplerate=self.sample_rate, channels=self.audio_data.shape[1], callback=self.audio_callback)
        self.stream.start()

    def audio_callback(self, outdata, frames, time, status):
        end_pos = min(self.position + frames, self.length)
        out_chunk = self.audio_data[self.position:end_pos]
        if end_pos - self.position < frames:
            out_chunk = np.pad(out_chunk, ((0, frames - (end_pos - self.position)), (0,0)), 'constant')
            self.stream.abort()
            self.timer.stop()
        outdata[:out_chunk.shape[0]] = out_chunk
        self.position += frames

    def update_cursor(self):
        self.cursor_left.setValue(self.position)
        self.cursor_right.setValue(self.position)
        if self.position >= self.length:
            self.timer.stop()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow(left_channel, right_channel, data, sample_rate)
    window.resize(1000, 600)
    window.show()
    sys.exit(app.exec())