from cmath import inf
from distutils.command.install_egg_info import to_filename
from math import comb
# from nis import cat
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from filehandler import FileHandler

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Meal Maker")
        self.filehandler = FileHandler()
        self.comboboxes = {}
        self.foods = self.filehandler.list_of_foods()

        self.app_ui()

    def app_ui(self):

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

        meal_page_layout = QVBoxLayout()
        meal_page_layout_title = QHBoxLayout()
        meal_page_layout_bottom = QHBoxLayout()
        meal_page_layout.addLayout(meal_page_layout_title)
        meal_page_layout.addLayout(meal_page_layout_bottom)
        meal_page_layout_left = QVBoxLayout()
        meal_page_layout_right = QVBoxLayout()
        meal_page_layout_bottom.addLayout(meal_page_layout_left)
        meal_page_layout_bottom.addLayout(meal_page_layout_right)

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

        menu_title = QLabel("Meal Maker")
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

        info_title = QLabel("Information")
        info_title.setAlignment(Qt.AlignCenter)
        info_page_layout.addWidget(info_title, 0, 0)
        info_title.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        info_content = QLabel("""Meal Maker is an application designed to help you with your weight loss journey. Our serves
provides an easy to use meal planner custom made by your own inputs based on your
personal tastes. Helping you to track and understand your calorie intake while providing you
tasty meals to kepp you motivated and enjoy your weight loss journey.

What will Meal Maker do?

After you have selected your preferred ingredients from the selection, in each category,
click calculate to have the macro nutrient values of the meal printed on the right side
of the screen!
""")
        info_content.setAlignment(Qt.AlignCenter)
        info_page_layout.addWidget(info_content, 1, 0)
        info_content.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        info_to_menu_btn = QPushButton("Back to menu")
        info_page_layout.addWidget(info_to_menu_btn, 2, 0)
        info_to_menu_btn.pressed.connect(self.info_to_menu)
        info_to_menu_btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

    # Meal Planning Page Widgets

        meal_title = QLabel("Meal Planner")
        meal_title.setAlignment(Qt.AlignCenter)
        meal_page_layout_title.addWidget(meal_title)
        meal_title.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # Combo Box's + Labels For Selecting Ingredients

        for category in self.foods:
            food_category = QLabel(category)
            meal_page_layout_left.addWidget(food_category)
            food_selection = QComboBox()
            food_selection.addItems(list(self.foods[category].keys()))
            meal_page_layout_left.addWidget(food_selection)
            self.comboboxes[category] = food_selection
        
    # Button to calculate inputs coresponding macro nutrients

        calculate_meal = QPushButton("Calculate!")
        meal_page_layout_left.addWidget(calculate_meal)
        calculate_meal.pressed.connect(self.calculate)

    # Right hand side widgets displaying Macro Nutriets of selected inputs

        final_meal = QLabel("Ingredients of Meal:")
        meal_page_layout_right.addWidget(final_meal)

        self.selected_meat = QLabel("Meat:")
        meal_page_layout_right.addWidget(self.selected_meat)

        self.selected_vitamin = QLabel("Vitamin:")
        meal_page_layout_right.addWidget(self.selected_vitamin)

        self.selected_seasoning = QLabel("Seasoning:")
        meal_page_layout_right.addWidget(self.selected_seasoning)

        self.selected_base = QLabel("Base:")
        meal_page_layout_right.addWidget(self.selected_base)

        meal_page_layout_right.addStretch(1)

        self.final_macros = QLabel("Macro Nutrients of Meal:")
        meal_page_layout_right.addWidget(self.final_macros)

        self.final_kcal = QLabel("Kcal:")
        meal_page_layout_right.addWidget(self.final_kcal)

        self.final_protein = QLabel("Protein:")
        meal_page_layout_right.addWidget(self.final_protein)

        self.final_fat = QLabel("Kcal:")
        meal_page_layout_right.addWidget(self.final_fat)

        self.final_carb = QLabel("Kcal:")
        meal_page_layout_right.addWidget(self.final_carb)
    
        cation_message = QLabel("Testing")
        meal_page_layout_right.addWidget(cation_message)

    # Button to return to menu page

        meal_to_menu_btn = QPushButton("Back to menu")
        meal_page_layout_right.addWidget(meal_to_menu_btn)
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

    # Fucntion to calucalte macro nutrients of selected foods!!!

    def calculate(self):
        food_selected = []
        for category in self.comboboxes:
            combo_box = self.comboboxes[category]
            if combo_box.currentText() == "":
                return
            foods = self.foods[category][combo_box.currentText()]
            food_selected.append(foods)

            if foods.category == "meat":
                self.selected_meat.setText(f"Meat: {foods.name}")
            elif foods.category == "vitamin":
                self.selected_vitamin.setText(f"Vitamin: {foods.name}")
            elif foods.category == "seasoning":
                self.selected_seasoning.setText(f"Seasoning: {foods.name}")
            else:
                self.selected_base.setText(f"Base: {foods.name}")

            # Calculates the macro nutriants
            kcal = 0
            protein = 0
            fat = 0
            carb = 0

            for foods in food_selected:
                kcal += foods.kcal
                protein += foods.protein
                fat += foods.fat
                carb += foods.carb

            self.final_kcal.setText(f"kcal: {kcal}")
            self.final_protein.setText(f"protein: {protein}")
            self.final_fat.setText(f"fat: {fat}")
            self.final_carb.setText(f"carb: {carb}")

app = QApplication()

window = MainWindow()
window.show()

app.exec()
