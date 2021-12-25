# Написать функцию по решению квадратных уравнений.


# Вычислить квадратное уравнение
#
# a(x**2) + bx + c = 0 (*)
#
# D = b**2 – 4ac;
#
# X1,2 = (-b +/- sqrt (D)) / 2a
#
# Предусмотреть 3 варианта:
# 1) Два действительных корня
# 2) Один действительный корень
# 3) Нет действительных корней

from typing import Union, NoReturn
from math import sqrt
from random import uniform


def quadratic_equation_func(a: Union[int, float],
                            b: Union[int, float],
                            c: Union[int, float]) -> NoReturn:

    disc_nant: float = b ** 2 - 4 * a * c
    print("Дискриминант D = {}".format(disc_nant))

    if disc_nant > 0:
        x1 = (-b + sqrt(disc_nant)) / (2 * a)
        x2 = (-b - sqrt(disc_nant)) / (2 * a)
        print("x1 = {} , x2 = {}".format(x1, x2))
    elif disc_nant == 0:
        x = -b / (2 * a)
        print("x = {}".format(x))
    else:
        print("Корней нет")


quadratic_equation_func(uniform(0, 10), uniform(0, 10), uniform(0, 10))
