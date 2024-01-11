from src.item import Item


class MixinChangeLang:
    """Класс миксин"""
    def __init__(self):
        self.__language = "EN"

    @property
    def language(self):
        """Геттер языка"""
        return self.__language

    def change_lang(self):
        """При вызове меняет язык"""
        if self.__language == "EN":
            self.__language = "RU"
        else:
            self.__language = "EN"


class Keyboard(Item, MixinChangeLang):
    """Инициализатор"""
    def __init__(self,  name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)
