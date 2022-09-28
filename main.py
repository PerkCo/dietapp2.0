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
        meal_page_layout.setRowStretch(0, 2)

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

    # Meal Planning Page Widgets

        meal_title = QLabel("Loren Ipsen")
        meal_title.setAlignment(Qt.AlignCenter)
        meal_page_layout.addWidget(meal_title, 0, 0, 1, 2)
        meal_title.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # Combo Box's + Labels For Selecting Ingredients

        base_label = QLabel("Base:")
        base_label.setAlignment(Qt.AlignCenter)
        meal_page_layout.addWidget(base_label, 1, 0)

        base_input = QComboBox()
        base_input.addItems(["Item 1", "Item 2"])
        meal_page_layout.addWidget(base_input, 2, 0)

        meat_label = QLabel("Meat:")
        meat_label.setAlignment(Qt.AlignCenter)
        meal_page_layout.addWidget(meat_label, 3, 0)

        meat_input = QComboBox()
        meat_input.addItems(["Item 1", "Item 2"])
        meal_page_layout.addWidget(meat_input, 4, 0)

        vitamin_label = QLabel("Vitamin:")
        vitamin_label.setAlignment(Qt.AlignCenter)
        meal_page_layout.addWidget(vitamin_label, 5, 0)

        vitamin_input = QComboBox()
        vitamin_input.addItems(["Item 1", "Item 2"])
        meal_page_layout.addWidget(vitamin_input, 6, 0)

        seasoning_label = QLabel("Seasoning:")
        seasoning_label.setAlignment(Qt.AlignCenter)
        meal_page_layout.addWidget(seasoning_label, 7, 0)

        seasoning_input= QComboBox()
        seasoning_input.addItems(["Item 1", "Item 2"])
        meal_page_layout.addWidget(seasoning_input, 8, 0)

    # Button to calculate inputs coresponding macro nutrients

        calculate_meal = QPushButton("Calculate!")
        meal_page_layout.addWidget(calculate_meal, 9, 0)

    # Right hand side widgets displaying Macro Nutriets of selected inputs

        meal_macros = QLabel("Loren Ipsen")
        meal_page_layout.addWidget(meal_macros)
    
        cation_message = QLabel("Testing")
        meal_page_layout.addWidget(cation_message)

    # Button to return to menu page

        meal_to_menu_btn = QPushButton("Back to menu")
        meal_page_layout.addWidget(meal_to_menu_btn)
        meal_to_menu_btn.pressed.connect(self.meal_to_menu)


    # Functions for switching stackwidgets (pages)

    def menu_to_info(self):
        self.stackwidget.setCurrentIndex(1)

    def menu_to_meal(self):
        self.stackwidget.setCurrentIndex(2)

    def info_to_menu(self):
        self.stackwidget.setCurrentIndex(0)

    def meal_to_menu(self):
        self.stackwidget.setCurrentIndex(0)

app = QApplication()

window = MainWindow()
window.show()

app.exec()
