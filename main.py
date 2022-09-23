from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        widget = QWidget()

        # Set the central widget of the Window.
        self.setCentralWidget(widget)


app = QApplication()

window = MainWindow()
window.show()

app.exec()
