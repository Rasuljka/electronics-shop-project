from src.item import Item


class Phone(Item):

    def __init__(self, name: str, price: float, quantity: int, sim_count):
        super().__init__(name, price, quantity)
        if float(sim_count) == int(sim_count) and int(sim_count) > 0:
            self.__sim_count = sim_count
        else:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля")

    def __add__(self, other):
        if isinstance(other, Item):
            return self.quantity + other.quantity
        elif isinstance(other, Phone):
            return self.quantity + other.quantity
        else:
            raise TypeError("Нельзя складывать с объектами других классов, кроме Item и Phone")

    def __repr__(self):
        """Информация для разработчиков"""
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    def __str__(self):
        """Информация для пользователей"""
        return self.name

    @property
    def number_of_sim(self):
        """Геттер sim- карт"""
        return self.__sim_count

    @number_of_sim.setter
    def number_of_sim(self, num):
        """Сеттер числа sim- карт"""
        if float(num) == int(num) and int(num) > 0:
            self.__sim_count = num
        else:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля")