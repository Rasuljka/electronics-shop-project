import pytest

from src.item import Item
from src.phone import Phone


@pytest.fixture
def samsung():
    return Phone("Samsung A22", 15000, 5, 2)


@pytest.fixture
def device():
    return Item("Калькулятор", 1000, 2)


def test_init(samsung):
    "Тест инициализатора"
    assert samsung.name == "Samsung A22"
    assert samsung.price == 15000
    assert samsung.quantity == 5
    assert samsung.number_of_sim == 2


def test_repr(samsung):
    """Тест информации для разработчика"""
    assert samsung.__repr__() == "Phone('Samsung A22', 15000, 5, 2)"


def test_str(samsung):
    """Тест информации для пользователя"""
    assert samsung.__str__() == "Samsung A22"


def test_add(device, samsung):
    """Тест сложения"""
    assert device + samsung == 7


def test_number_of_sim(samsung):
    """Тест количества sim- карт"""
    assert samsung.number_of_sim == 2
    samsung.number_of_sim = 3
    assert samsung.number_of_sim == 3
