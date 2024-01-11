import pytest
from src.keyboard import Keyboard


@pytest.fixture
def samsung():
    return Keyboard("Samsung", 15000, 5)


def test_init(samsung):
    "Тест инициализатора"
    assert samsung.name == "Samsung"
    assert samsung.price == 15000
    assert samsung.quantity == 5


def test_language(samsung):
    """Тест геттера языка"""
    assert samsung.language == "EN"


def test_change_lang(samsung):
    """Тест смены языка"""
    samsung.change_lang()
    assert str(samsung.language) == "RU"
    samsung.change_lang()
    assert str(samsung.language) == "EN"
    samsung.change_lang()
    assert str(samsung.language) == "RU"
    with pytest.raises(AttributeError):
        samsung.language = "CH"
