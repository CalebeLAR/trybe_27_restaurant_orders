from csv import DictReader, DictWriter
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


def write_csv_inventory(
    recipe: Recipe, inventory_file_path=BASE_INVENTORY
) -> None:
    inventory = read_csv_inventory(inventory_file_path)

    for ingredient, amount in recipe.items():
        inventory[ingredient] = inventory.get(ingredient) - amount

    with open(inventory_file_path, "w", newline="") as file:
        fieldnames = ["ingredient", "initial_amount"]
        writer = DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        for ingredient, amount in inventory.items():
            writer.writerow(
                {"ingredient": ingredient.name, "initial_amount": amount}
            )

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
            if (
                ingredient not in self.inventory
                or amount > inventory_amount
            ):
                return False

        return True

    # Req 5.2
    def consume_recipe(self, recipe: Recipe) -> None:
        is_availability = self.check_recipe_availability(recipe)

        # lança uma exceção caso o ingrediente não esteja disponível
        if is_availability is False:
            raise ValueError("recipe not availability")

        self.inventory = write_csv_inventory(recipe)


def requisito05():
    carne = Ingredient("lim\xe3o")
    recipe = {carne: 30}

    inventoryMapping = InventoryMapping()
    print(inventoryMapping.check_recipe_availability(recipe))
    # inventoryMapping.consume_recipe(recipe)
    # print(inventoryMapping.inventory[carne])


def test_write():
    recipe = {Ingredient("carne"): 10}
    print(read_csv_inventory(BASE_INVENTORY).get(Ingredient("carne")))
    write_csv_inventory(recipe)
    print(read_csv_inventory(BASE_INVENTORY).get(Ingredient("carne")))


def test_do_test():
    ingredient_1 = Ingredient("limão")
    ingredient_2 = Ingredient("fermento")

    amount_1 = 250
    amount_2 = 201

    mapping = InventoryMapping()
    is_recipe_available = mapping.check_recipe_availability(
        {ingredient_1: amount_1, ingredient_2: amount_2}
    )

    print(is_recipe_available)


# test_do_test()
