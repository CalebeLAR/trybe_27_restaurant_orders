import csv
from models.dish import Dish
from models.ingredient import Ingredient


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.source_path = source_path
        self.dishes = set()
        self.assemble_dishes_from_the_menu()

    def assemble_dishes_from_the_menu(self):
        """ le o arquivo e insere no set dishes todos os pratos montados ja com
        seus ingredientes"""

        with open(self.source_path) as menu_data_file:
            menu_data = csv.reader(menu_data_file)
            header, *menu_data = menu_data

            # insere cada para pelo nome no set dishes
            for menu in menu_data:
                dish, price, ingredient, amount = menu

                dish = Dish(dish, float(price))
                ingredient = Ingredient(ingredient)

                # adiciona o prato vazio em dish caso ja não esteja lá
                if dish not in self.dishes:
                    self.dishes.add(dish)

                # adiona um ingrediente para cada prato vazio em self.dishes
                for dish_already_added in self.dishes:
                    if dish_already_added.name == dish.name:
                        dish_already_added.add_ingredient_dependency(
                            ingredient, int(amount)
                        )
