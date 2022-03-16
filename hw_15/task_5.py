# Ex.5
# Реализовать класс Car в соответствии с интерфейсом.
# В нем реализовать метод speed, возвращающий текущую скорость.
# Реализовать декоратор метода - в случае превышения скорости - декоратор
# должен логировать в logger.error сообщение о превышении лимита


from datetime import datetime
from typing import Dict, Any
from functools import wraps
from task_4 import ABCCar


logger_error: Dict[str, Any] = {}


def speed_limit_deco(method):

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        method(self, *args, **kwargs)
        message_time = datetime.now()
        logger_error[f'Over speed {message_time}'] = self.speed if self.speed > 90 else ...

    return wrapper


class Car(ABCCar):

    def __init__(self, brand: str, model: str, year_of_manufacture: str, speed: int or float = 0) -> None:
        self._brand = brand
        self._model = model
        self._year_of_manufacture = year_of_manufacture
        self._speed = speed

    @property
    def get_brand(self) -> str:
        return self._brand

    @property
    def get_model(self) -> str:
        return self._model

    @property
    def get_year_of_manufacture(self) -> str:
        return self._year_of_manufacture

    @property
    def speed(self) -> int:
        return self._speed

    @speed.setter
    @speed_limit_deco
    def speed(self, speed: int or float):
        self._speed = speed

    @property
    def get_full_info(self) -> Dict[str, Any]:
        return {'brand': f'{self._brand}',
                'model': f'{self._model}',
                'year of manufacture': f'{self._year_of_manufacture}',
                'current speed': f'{self._speed}'}


if __name__ == '__main__':
    car = Car('Audi', 'RS2', '1993', speed=90)
    car.speed = 120
    print(car.speed)
    print(logger_error)
    car.speed = 130
    print(logger_error)
    print(car.speed)
