from typing import Dict, List

from services.inventory_control import InventoryMapping
from services.menu_data import MenuData

DATA_PATH = "data/menu_base_data.csv"
INVENTORY_PATH = "data/inventory_base_data.csv"


class MenuBuilder:
    def __init__(self, data_path=DATA_PATH, inventory_path=INVENTORY_PATH):
        self.menu_data = MenuData(data_path)
        self.inventory = InventoryMapping(inventory_path)

    def make_order(self, dish_name: str) -> None:
        try:
            curr_dish = [
                dish
                for dish in self.menu_data.dishes
                if dish.name == dish_name
            ][0]
        except IndexError:
            raise ValueError("Dish does not exist")

        self.inventory.consume_recipe(curr_dish.recipe)

    # Req 4
    def get_main_menu(self, restriction=None) -> List[Dict]:
        """recebe uma restrição alimentar e monta um menu só com os pratos que
        não possuem essa restrição"""
        menu = []

        # itera sobre todos os pratos do menu separando suas restições
        for dish in self.menu_data.dishes:
            restrictions = dish.get_restrictions()

            is_availability = self.inventory.check_recipe_availability(
                dish.recipe
            )

            # inclui o prato caso ele não possua a restrição
            if str(restriction) not in str(restrictions) and is_availability:
                menu.append(
                    {
                        "dish_name": dish.name,
                        "ingredients": dish.get_ingredients(),
                        "price": dish.price,
                        "restrictions": dish.get_restrictions(),
                    }
                )

        return menu


menuBuilder = MenuBuilder()
menu = menuBuilder.get_main_menu('ANIMAL_MEAT')
print(menu)
