from src.item import Item


class Phone(Item):

    def __init__(self, name: str, price: float, quantity: int, sim: int):
        super().__init__(name, price, quantity)
        self.__number_of_sim = sim

    def __repr__(self):
        return f"{super().__repr__()[:-1]}, {self.number_of_sim})"

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, sim):
        if isinstance(sim, int) and sim > 0:
            self.__number_of_sim = sim
        else:
            print('Количество физических SIM-карт должно быть целым числом больше нуля')
