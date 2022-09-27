from cmath import inf
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Diet App")

        widget = QWidget()

        # Set the central widget of the Window.
        self.setCentralWidget(widget)
        
        layout = QVBoxLayout()

        menu_page_layout = QGridLayout()

        info_page_layout = QGridLayout()

        meal_page_layout = QGridLayout()

        menu_page = QWidget()
        menu_page.setLayout(menu_page_layout)

        info_page = QWidget()
        info_page.setLayout(info_page_layout)

        meal_page = QWidget()
        meal_page.setLayout(meal_page_layout)


        self.stackwidget = QStackedWidget()
        self.stackwidget.addWidget(menu_page)
        self.stackwidget.addWidget(info_page)
        self.stackwidget.addWidget(meal_page)

        self.stackwidget.setCurrentIndex(0)
        self.stackwidget.setLayout(layout)
        self.setCentralWidget(self.stackwidget)

app = QApplication()

window = MainWindow()
window.show()

app.exec()
