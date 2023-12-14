"""Здесь надо написать тесты с использованием pytest для модуля item."""

from src.item import Item

item3 = Item("Ноутбук", 5000, 2)
assert item3.name == "Ноутбук"
assert item3.price == 5000
assert item3.quantity == 2
assert item3.calculate_total_price() == 10000