from cmath import inf
from distutils.command.install_egg_info import to_filename
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
        menu_page_layout.setRowStretch(0, 2)
        menu_page_layout.setRowStretch(1, 1)

        info_page_layout = QGridLayout()
        info_page_layout.setRowStretch(0, 1)
        info_page_layout.setRowStretch(1, 2)
        info_page_layout.setRowStretch(2, 1)


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

    # Menu Page Widgets

        menu_title = QLabel("Loren Epsin")
        menu_title.setAlignment(Qt.AlignCenter)
        menu_page_layout.addWidget(menu_title, 0, 0, 1, 2)
        menu_title.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        menu_to_info_btn = QPushButton("Information")
        menu_page_layout.addWidget(menu_to_info_btn, 1, 0)
        menu_to_info_btn.pressed.connect(self.menu_to_info)
        menu_to_info_btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        menu_to_meal_btn = QPushButton("Meal Planner")
        menu_page_layout.addWidget(menu_to_meal_btn, 1, 1)
        menu_to_meal_btn.pressed.connect(self.menu_to_meal)
        menu_to_meal_btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

    # Infomation Page Widgets

        info_title = QLabel("Loren Epsin")
        info_title.setAlignment(Qt.AlignCenter)
        info_page_layout.addWidget(info_title, 0, 0)
        info_title.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        info_content = QLabel("""Loren Epsin 
omml
manwey is hot""")
        info_content.setAlignment(Qt.AlignCenter)
        info_page_layout.addWidget(info_content, 1, 0)
        info_content.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        info_to_menu_btn = QPushButton("Back to menu")
        info_page_layout.addWidget(info_to_menu_btn, 2, 0)
        info_to_menu_btn.pressed.connect(self.info_to_menu)
        info_to_menu_btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

    # Functions for switching stackwidgets (pages)

    def menu_to_info(self):
        self.stackwidget.setCurrentIndex(1)

    def menu_to_meal(self):
        self.stackwidget.setCurrentIndex(2)

    def info_to_menu(self):
        self.stackwidget.setCurrentIndex(0)

app = QApplication()

window = MainWindow()
window.show()

app.exec()
