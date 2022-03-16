# Ex.4
# Реализовать интерфейс класса Car.


import abc


class ABCCar(abc.ABC):

    @abc.abstractmethod
    def get_brand(self):
        pass

    @abc.abstractmethod
    def get_model(self):
        pass

    @abc.abstractmethod
    def get_year_of_manufacture(self):
        pass

    @abc.abstractmethod
    def get_full_info(self):
        pass
