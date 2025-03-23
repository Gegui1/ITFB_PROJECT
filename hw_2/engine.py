"""
create dataclass `Engine`
"""

from dataclasses import dataclass

@dataclass
class Engine:
    volume: float  # объем двигателя
    pistons: int   # количество цилиндров

    def __post_init__(self):
        self._volume = self.volume
        self._pistons = self.pistons

    @property
    def volume(self):
        """Геттер для объема двигателя"""
        return self._volume

    @volume.setter
    def volume(self, value):
        """Сеттер с проверкой"""
        if value <= 0:
            raise ValueError("Объем двигателя должен быть положительным!")
        self._volume = value

    @property
    def pistons(self):
        """Геттер для количества цилиндров"""
        return self._pistons

    @pistons.setter
    def pistons(self, value):
        """Сеттер с проверкой"""
        if value <= 0:
            raise ValueError("Количество цилиндров должно быть положительным!")
        self._pistons = value