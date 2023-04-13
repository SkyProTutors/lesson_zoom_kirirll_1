# from Class_work.class_work import Animal
#
#
# def test_init():
#     an_test = Animal("Cat", 7)
#     assert an_test.specie == "Cat"
#     assert an_test.age == 7
#
import pytest


def test_init(test_animal):
    assert test_animal.specie == "Cat"
    assert test_animal.age == 7


def test_eat(test_animal):
    assert test_animal.eat() == f"Cat, кушает 2 раза в день"

def test_specie(test_animal):
    test_animal.specie = "Dog"
    assert test_animal.specie == "Dog"
    with pytest.raises(Exception):
        test_animal.specie = "SuperDog"

