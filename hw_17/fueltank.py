

from typing import Union

from abc_classes import ABCFuelTank
from my_exception import FuelFinishError


class FuelTank(ABCFuelTank):

    def __init__(self, tank_size: int):
        self._tank_size = tank_size
        self._fuel_lvl = tank_size

    @property
    def tank_size(self) -> int:
        return self._tank_size

    @property
    def fuel_lvl(self) -> int:
        return self._fuel_lvl

    def increase_fuel_lvl(self, liters: int) -> None:
        self._fuel_lvl += liters

    def decrease_fuel_lvl(self, liters: Union[int, float]) -> None:
        condition = self._fuel_lvl < 2
        if condition:
            raise FuelFinishError(f'Low fuel level {self._fuel_lvl}')
        self._fuel_lvl -= liters
