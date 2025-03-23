"""
создайте класс `Plane`, наследник `Vehicle`
"""


from hw_2.base import Vehicle
from hw_2 import exceptions

class Plane(Vehicle):
    def __init__(self, weight, fuel, fuel_consumption, max_cargo, cargo=0, started=False):
        super().__init__(weight, fuel, fuel_consumption, started)
        self._max_cargo = max_cargo
        self._cargo = cargo

    @property
    def max_cargo(self):
        return self._max_cargo

    @max_cargo.setter
    def max_cargo(self, volue):
        if volue < 0:
            raise ValueError("Максимальный груз не может быть отрицательным!")
        self._max_cargo = volue

    @property
    def cargo(self):
        return self._cargo

    @cargo.setter
    def cargo(self, value):
        if value < 0:
            raise ValueError("Количество груза не может быть отрицательным!")
        if value > self._max_cargo:
            raise exceptions.CargoOverload("Перегруз!")
        self._cargo = value

    def load_cargo(self, cargo_to_load):
        if self._cargo + cargo_to_load > self.max_cargo:
            raise exceptions.CargoOverload("Перегруз!")
        self._cargo += cargo_to_load

    def remove_all_cargo(self):
        old_cargo = self._cargo
        self._cargo = 0
        return old_cargo