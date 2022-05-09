

from random import shuffle, choice
from typing import List
from datetime import datetime

from abc_classes import ABCNavigator
from my_exception import StopDrive, SpeedLimitError, ArriveWarning


class Navigator(ABCNavigator):

    def __init__(self, car):
        self.destination_point = 0
        self.speed_limit = 0
        self.logs = {car: {}}
        self._logging_points = []

    def speed_limit_warning(self):
        speed_limit_signs = [0 for _ in range(20)] + [40, 60, 90, 120]
        shuffle(speed_limit_signs)
        sing = choice(speed_limit_signs)
        if sing:
            self.speed_limit = sing
            raise SpeedLimitError(f'Attention speed limit {sing} km/h')

    def set_destination_point(self, odometer_value: int, travel_length: int) -> None:
        if not isinstance(travel_length, int):
            raise TypeError
        elif travel_length <= 0:
            raise ValueError
        self.destination_point = odometer_value + travel_length

    def logging_points(self, speed: int) -> List[int]:
        condition = speed % 10
        range_condition = speed // 10 + 1 if condition else int(speed / 10)
        self._logging_points = [10 for _ in range(range_condition)]
        self._logging_points[-1] = condition if condition else 10
        return self._logging_points

    def logging(self, car) -> None:
        self.logs[car].update({
            f'{datetime.now()}': {
                'mileage': car.mileage,
                'speed': car.speed,
                'consumption per 100 km': car.current_consumption,
                'fuel level': car.tank.fuel_lvl,
            }
        })

    def destination_warning(self, odometer_value: int) -> None:
        last_few_km = self.destination_point - odometer_value
        first_condition = odometer_value >= self.destination_point
        second_condition = last_few_km <= 10

        if first_condition:
            raise StopDrive('You are arrived. Good bye...')
        elif second_condition:
            self.speed_limit = last_few_km
            raise ArriveWarning(f'You will soon arrive at your destination point. {last_few_km} kilometers left.')
