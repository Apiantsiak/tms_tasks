# Ex.4
# Реализовать интерфейс класса Car.


import abc


class ABCCar(abc.ABC):

    @abc.abstractmethod
    def brand(self):
        pass

    @abc.abstractmethod
    def model(self):
        pass

    @abc.abstractmethod
    def year_of_manufacture(self):
        pass

    @abc.abstractmethod
    def full_info(self):
        pass
