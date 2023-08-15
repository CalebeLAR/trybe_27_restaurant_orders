from csv import DictReader
from typing import Dict

# retirei o 'src.' das importaçoes pois estava dando erro
from models.dish import Recipe
from models.ingredient import Ingredient

BASE_INVENTORY = "data/inventory_base_data.csv"

Inventory = Dict[Ingredient, int]


def read_csv_inventory(inventory_file_path=BASE_INVENTORY) -> Inventory:
    inventory = dict()

    with open(inventory_file_path, encoding="utf-8") as file:
        for row in DictReader(file):
            ingredient = Ingredient(row["ingredient"])
            inventory[ingredient] = int(row["initial_amount"])

    return inventory


# Req 5
class InventoryMapping:
    def __init__(self, inventory_file_path=BASE_INVENTORY) -> None:
        self.inventory = read_csv_inventory(inventory_file_path)

    # Req 5.1
    def check_recipe_availability(self, recipe: Recipe) -> bool:
        """verifica se tem em estoque o ingrediente e aquantidade necessária
        para fazer a receita, se tiver retorna True, se não retorna False"""

        # acessa o ingrediente e a quantidade na receita
        for ingredient, amount in recipe.items():
            inventory_amount = self.inventory.get(ingredient)

            # verifica se tem no estoque a quantidade do ingrediente que a
            # receita precisa
            if ingredient not in self.inventory or amount > inventory_amount:
                return False

        return True

    # Req 5.2
    def consume_recipe(self, recipe: Recipe) -> None:
        """lança um erro de valor caso a receita não seja viável e caso seja
        viável atualiza o inventário para guardar a nova quantidade do
        ingrediente"""

        is_availability = self.check_recipe_availability(recipe)

        # lança uma exceção caso o ingrediente não esteja disponível
        if is_availability is False:
            raise ValueError("recipe not availability")

        # atualiza a quantidade de ingrediente no inventário
        for ingredient, amount in recipe.items():
            self.inventory[ingredient] -= amount
