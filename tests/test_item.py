"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture
def device():
    return Item("Калькулятор", 1000, 2)


def test___init__():
    item3 = Item("Ноутбук", 5000, 2)
    assert item3.name == "Ноутбук"
    assert item3.price == 5000
    assert item3.quantity == 2


def test_calculate_total_price():
    item3 = Item("Ноутбук", 5000, 2)
    assert item3.calculate_total_price() == 10000


def test_apply_discount():
    item3 = Item("Ноутбук", 5000, 2)
    assert item3.apply_discount() is None


def test_name_property():
    """Переименование"""
    item3 = Item("ПерсональныйКомпьютер", 15000, 2)
    assert item3.name == 'ПерсональныйКомпьютер'


def test_name_setter(device):
    device.name = "ПерсональныйКомпьютер"
    assert device.name == "Персональн"


def test_instantiate_from_csv():
    """Достаем из csv объекты класса"""
    Item.instantiate_from_csv('src/items.csv')

    assert len(Item.all) == 5
    assert Item.all[0].name == "Смартфон"
    assert Item.all[2].price == 10
    assert Item.all[3].quantity == 5


def test_string_to_number_static():
    """Преобразование строки в целое число"""
    assert Item.string_to_number("5.65") == 5