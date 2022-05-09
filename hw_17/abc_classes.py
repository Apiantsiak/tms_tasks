

from typing import Union
import abc


class ABCCar(abc.ABC):

    @abc.abstractmethod
    def move_forward(self, distance: int):
        pass

    @abc.abstractmethod
    def stop(self):
        pass

    @abc.abstractmethod
    def fill_up_tank(self, liters: Union[int, float]):
        pass

    @abc.abstractmethod
    def dynamic_driving_range(self):
        pass


class ABCFuelTank(abc.ABC):

    @abc.abstractmethod
    def tank_size(self):
        return self._tank_size

    @abc.abstractmethod
    def fuel_lvl(self):
        pass

    @abc.abstractmethod
    def increase_fuel_lvl(self, liters: int):
        pass

    @abc.abstractmethod
    def decrease_fuel_lvl(self, liters: Union[int, float]):
        pass


class ABCNavigator(abc.ABC):

    @abc.abstractmethod
    def speed_limit_warning(self):
        pass

    @abc.abstractmethod
    def set_destination_point(self, odometer_value: int, distance: int):
        pass
