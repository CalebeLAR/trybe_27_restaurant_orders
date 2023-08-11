from src.models.dish import Dish  # noqa: F401, E261, E501
from pytest import raises
from src.models.ingredient import Ingredient


# Req 2
def test_dish():
    # a classe pode ser instanciada corretamente de acordo com a assinatura
    # esperada;
    dish = Dish("Dish", 10.00)
    assert isinstance(dish, Dish)
    assert dish.name == "Dish"
    assert dish.price == 10.00

    # __repr__
    dish = Dish("Dish", 10.00)
    assert repr(dish) == "Dish('Dish', R$10.00)"

    # __eq__
    dish = Dish("Dish", 10.00)
    dish_copy = Dish("Dish", 10.00)
    assert dish == dish_copy

    # __hash__
    dish = Dish("Dish", 10.00)
    assert hash("Dish('Dish', R$10.00)") == hash(dish)

    # add_ingredient_dependency
    ingredient = Ingredient("farinha")
    dish = Dish("Dish", 10.00)
    dish.add_ingredient_dependency(ingredient, 3)
    assert dish.recipe == {ingredient: 3}

    # get_ingredients
    restrictions = dish.get_restrictions()
    assert isinstance(restrictions, set)
    assert "<Restriction.GLUTEN: 'GLUTEN'>" in str(restrictions)

    # get_restrictions
    ingredients = dish.get_ingredients()
    assert str(ingredients) == "{Ingredient('farinha')}"

    # são levantados erros ao criar pratos inválidos;
    with raises(TypeError, match="Dish price must be float."):
        dish = Dish("Dish", "10.00")

    with raises(ValueError, match="Dish price must be greater then zero."):
        dish = Dish("Dish", -10.00)
