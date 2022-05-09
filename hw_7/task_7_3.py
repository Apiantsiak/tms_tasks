# Описать функцию Sin1( x , ε ) вещественного типа 
# (параметры x , ε — вещественные, ε > 0), находящую приближенное значение функции sin( x ):
#
# sin( x ) = x – x ^3 /(3!) + x^ 5 /(5!) – ... + (–1) ^ n · x^( 2·n+1) /((2· n +1)!) + ... .
#
# В сумме учитывать все слагаемые, модуль которых больше ε.
# С помощью Sin1 найти приближенное значение синуса для данного x при шести данных ε


from math import sin
from random import randint


def sin1_func(x_val, eps_val) -> float:
    if eps_val <= 0:
        print("Epsilon should be greater than 0")
    y = x_val
    result = x_val
    i = 3
    while abs(y) > eps:
        y *= (-1) * x_val * x_val / ((i - 1) * i)
        result += y
        i += 2
    return result


x: int = randint(1, 10)
eps: float = 0.1

for _ in range(6):
    print(f"eps = {eps}",
          f"sin({x}) = {sin1_func(x, eps_val=eps)}",
          f"Value for validation {sin(x)}", sep="\n")
    eps /= 10
