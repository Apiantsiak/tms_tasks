# Ex.5
# Реализовать класс Car в соответствии с интерфейсом.
# В нем реализовать метод speed, возвращающий текущую скорость.
# Реализовать декоратор метода - в случае превышения скорости - декоратор
# должен логировать в logger.error сообщение о превышении лимита


from datetime import datetime
from typing import Dict, Any
from functools import wraps
from task_4 import ABCCar
from task_6 import SpoilerMixin


def speed_limit_deco(method):

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        method(self, *args, **kwargs)
        speed = self.speed
        if speed > 90:
            error_time = f"{datetime.now().strftime('%x')} {datetime.now().strftime('%X')}"
            error_mes = f"Over speed limit {error_time}: {self.brand} {self.model}"
            self.logger_errors[error_mes] = speed
            return speed
        else:
            return speed

    return wrapper


class Car(SpoilerMixin, ABCCar):

    logger_errors: Dict[str, Any] = {}

    def __init__(self, brand: str, model: str, year_of_manufacture: str, speed: int or float = 0) -> None:
        self._brand = brand
        self._model = model
        self._year_of_manufacture = year_of_manufacture
        self._speed = speed
        super().__init__()

    @property
    def brand(self) -> str:
        return self._brand

    @property
    def model(self) -> str:
        return self._model

    @property
    def year_of_manufacture(self) -> str:
        return self._year_of_manufacture

    @property
    def speed(self) -> int:
        return self._speed

    @speed.setter
    @speed_limit_deco
    def speed(self, speed: int or float):
        if self.spoiler:
            self._speed = speed + 10
        else:
            self._speed = speed

    @property
    def full_info(self) -> Dict[str, Any]:
        return {'brand': f'{self._brand}',
                'model': f'{self._model}',
                'year of manufacture': f'{self._year_of_manufacture}',
                'current speed': f'{self._speed}'}


if __name__ == '__main__':

    car_audi = Car('Audi', 'RS2', '1993', speed=90)
    car_vw = Car("VW", "Golf MK2", "1990", speed=80)
