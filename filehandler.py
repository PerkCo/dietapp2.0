import json


import json

from Food import Food

class FileHandler:
    @staticmethod
    def get_json_foods():
        with open("foods.json", "r") as file:
            data = json.load(file)

            return data

    def list_of_foods(self) -> list[Food]:
        data = self.get_json_foods()
        food_data = {}
        for category in data:
            food_data[category] = {}
            for food in data[category]:
                food_data[category][food["name"]] = Food(food["name"], food["kcal"], food["protien"],
                                                        food["fat"], food["carb"], category)
                
            return food_data