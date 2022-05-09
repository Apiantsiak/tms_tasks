

from typing import Union, Dict, Tuple
import pytest

from abc_classes import ABCCar
from fueltank import FuelTank
from navigator import Navigator
from spoiler import SpoilerMixin
from my_exception import StopDrive, FuelFinishError, SpeedLimitError, ArriveWarning


class Car(ABCCar, SpoilerMixin):

    _fuel_consumption_data: Dict[Tuple[int, int], Union[int, float]] = {
        (0, 40): 10,
        (40, 60): 8,
        (60, 90): 6,
        (90, 120): 5.5,
        (120, 140): 8,
        (140, 180): 11,
    }

    def __init__(self, brand: str, model: str, tank_size: int,
                 mileage: int = 0, spoiler: bool = False, speed: int = 30) -> None:
        self._brand = brand
        self._model = model
        self.navigator = Navigator(self)
        self.tank = FuelTank(tank_size)
        self.spoiler = spoiler
        self.mileage = mileage
        self.speed = speed
        self.driving_range = 0
        self.current_consumption = 0

    def calculate_consumption(self, km: int = 0) -> float:
        self.current_consumption = sum([
            consumption for speed_range, consumption in self._fuel_consumption_data.items()
            if self.speed in range(*speed_range)
        ])

        fuel_consumption_per_km = round(self.current_consumption / 100, 3)
        fuel_consumption = km * fuel_consumption_per_km

        return fuel_consumption

    def odometer(self, traveled_distance: int) -> None:
        self.mileage += traveled_distance

    def move_forward(self, distance: int) -> None:
        try:
            flag = True
            self.navigator.set_destination_point(odometer_value=self.mileage, travel_length=distance)
        except (ValueError, TypeError):
            print('Invalid value entered! The value must be an integer and greater than zero.')
            flag = False

        while flag:
            try:
                for km in self.navigator.logging_points(self.speed):
                    self.odometer(km)
                    self.tank.decrease_fuel_lvl(self.calculate_consumption(km))
                    self.dynamic_driving_range()
                    self.navigator.logging(self)
                    self.navigator.speed_limit_warning()
                    self.navigator.destination_warning(self.mileage)
                self.acceleration()
            except SpeedLimitError as error:
                print(f'\n{error}\n')
                condition = self.speed > self.navigator.speed_limit
                if condition:
                    self.speed = self.navigator.speed_limit
            except FuelFinishError as error:
                print(f'\n{error}\n')
                self.fill_up_tank(self.tank.tank_size - self.tank.fuel_lvl)
                self.speed = 30
            except ArriveWarning as error:
                print(f'\n{error}\n')
                self.speed = self.navigator.speed_limit
            except StopDrive as error:
                print(f'\n{error}\n')
                self.stop()
                break

    def stop(self) -> None:
        self.speed = 0

    def acceleration(self) -> None:
        if self.spoiler:
            super().acceleration()
        else:
            self.speed += 5

    def fill_up_tank(self, liters: Union[int, float]) -> None:
        self.tank.increase_fuel_lvl(liters)

    def dynamic_driving_range(self) -> int:
        self.calculate_consumption()
        self.driving_range = int(self.tank.fuel_lvl * (100 / self.current_consumption))
        return self.driving_range
