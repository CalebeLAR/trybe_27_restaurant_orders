from src.models.ingredient import Ingredient  # noqa: F401, E261, E501


# Req 1
def test_ingredient(capsys):
    # a classe pode ser instanciada corretamente de acordo com a assinatura
    # esperada;
    ingredient1 = Ingredient("massa de ravioli")
    ingredient2 = Ingredient("massa de ravioli")
    ingredient3 = Ingredient("massa de lasanha")
    assert isinstance(ingredient1, Ingredient)

    # o atributo conjunto restrictions é populado como esperado;
    assert isinstance(ingredient1.restrictions, set)
    assert "<Restriction.GLUTEN: 'GLUTEN'>" in str(ingredient1.restrictions)
    assert "<Restriction.LACTOSE: 'LACTOSE'>" in str(ingredient1.restrictions)

    # o método mágico __repr__ funcione como esperado;
    assert repr(ingredient1) == "Ingredient('massa de ravioli')"

    # o método mágico __eq__ funcione como esperado;
    assert ingredient1 != ingredient3
    assert ingredient1 == ingredient2

    # o método mágico __hash__ funcione como esperado.
    assert hash(ingredient3.name) == hash(ingredient3)
