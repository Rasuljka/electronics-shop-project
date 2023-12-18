"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item


@pytest.fixture
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
