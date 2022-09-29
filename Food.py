from dataclasses import dataclass
from unicodedata import category

@dataclass
class Food:
    name: str
    kcal: float
    protien: float
    fat: float
    carb: float
    category: str