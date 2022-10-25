from dataclasses import dataclass

#Assings values (str, float) to each value for dictionarys in food.json
@dataclass
class Food:
    name: str
    kcal: float
    protein: float
    fat: float
    carb: float
    category: str