from Class_work.class_work import Animal
import pytest


@pytest.fixture
def test_animal():
    animal = Animal("Cat", 7)
    return animal
