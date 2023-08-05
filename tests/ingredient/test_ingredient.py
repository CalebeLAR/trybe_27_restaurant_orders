from src.models.ingredient import Ingredient, Restriction  # noqa: F401, E261, E501


# Req 1
def test_ingredient(capsys):
    # a classe pode ser instanciada corretamente de acordo com a assinatura
    # esperada;
    ingredient0 = Ingredient("")
    ingredient1 = Ingredient("massa de ravioli")
    assert isinstance(ingredient1, Ingredient)

    # o atributo conjunto restrictions é populado como esperado;
    assert ingredient1.restrictions == {
        Restriction.LACTOSE,
        Restriction.GLUTEN,
    }
    assert ingredient0.restrictions == set()

    # o método mágico __repr__ funcione como esperado;
    print(repr(ingredient1))
    captured = capsys.readouterr()
    assert captured.out == "Ingredient('massa de ravioli')\n"

    print(repr(ingredient0))
    captured = capsys.readouterr()
    assert captured.out == "Ingredient('')\n"

    # o método mágico __eq__ funcione como esperado;
    ingredient1 = Ingredient("massa de ravioli")
    ingredient2 = Ingredient("massa de ravioli")
    ingredient3 = Ingredient("massa de lasanha")

    assert ingredient1 != ingredient3
    assert ingredient1 == ingredient2

    # o método mágico __hash__ funcione como esperado.
    assert hash(ingredient3.name) == hash(ingredient3)
