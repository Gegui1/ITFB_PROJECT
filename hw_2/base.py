from hw_2.exceptions import LowFuelError, NotEnoughFuel
from abc import ABC

class Vehicle(ABC):
    def __init__(self, weight=0, fuel=0, fuel_consumption=0, started=False):
        self.weight = weight
        self.started = started
        self._fuel = fuel
        self._fuel_consumption = fuel_consumption

    @property
    def fuel(self):
        return self._fuel

    @fuel.setter
    def fuel(self, value):
        if value < 0:
            raise ValueError("Количество топлива не может быть отрицательным!")
        self._fuel = value

    @property
    def fuel_consumption(self):
        return self._fuel_consumption

    @fuel_consumption.setter
    def fuel_consumption(self, value):
        if value < 0:
            raise ValueError("Расход топлива не может быть отрицательным!")
        self._fuel_consumption = value

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError("Недостаточно топлива для запуска.")

    def move(self, distance):
        if not self.started:
            raise ValueError("Двигатель не запущен.")
        required_fuel = (distance * self.fuel_consumption) / 100
        if required_fuel > self.fuel:
            raise NotEnoughFuel("Недостаточно топлива.")
        self.fuel -= required_fuel
