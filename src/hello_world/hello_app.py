from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton
from PySide6.QtCore import QSize, Qt
import sys

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    
    self.setWindowTitle("Hello App")
    button = QPushButton("Press!")
    
    self.setFixedSize(QSize(400, 300))
    
    # setCentralWidget puts the button in the middle of the window
    # by default the button will take up the whole window
    self.setCentralWidget(button)

# only one per application
# holds the event loop
# each event found waiting in the event queue is passed to the specific event handler
# event handler does its thing then passes control back to the event loop
app = QApplication(sys.argv)

# a widget is a window by default
# if you declare any individual object (eg a button), it will create a window with just that object
# but you can nest widgets
# window = QWidget()
# window = QMainWindow() # preferable to QWidget
window = MainWindow()

window.show()

app.exec()
# when the window is closed, the app stops running