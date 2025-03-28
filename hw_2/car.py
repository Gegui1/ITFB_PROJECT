"""
создайте класс `Car`, наследник `Vehicle`
"""

from hw_2.base import Vehicle
from hw_2.engine import Engine
from hw_2.exceptions import *

class Car(Vehicle):
    def __init__(self, weight: int, fuel: float, fuel_consumption: float, engine=None, started=False):
        super().__init__(weight, fuel, fuel_consumption, started)
        self._engine = engine

    def start(self):
        if self.started:
            raise ValueError("Двигатель уже запущен.")
        if self.fuel == 0:
            raise LowFuelError("Недостаточно топлива для запуска.")
        self.started = True

    @property
    def engine(self):
        return self._engine

    @engine.setter
    def engine(self, engine: Engine):
        if not isinstance(engine, Engine):
            raise ValueError("Объект должен быть экземпляром класса Engine.")
        self._engine = engine

    def set_engine(self, engine: Engine):
        self.engine = engine
