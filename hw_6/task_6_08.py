# Написать функцию принимающая на вход неопределенным количеством аргументов
# и именованный аргумент mean_type. В зависимости от mean_type вернуть
# среднеарифметическое либо среднегеометрическое. Написать программу в виде трех функций.


from random import randint
from typing import List


def avg_calc_func(*args: int, mean_type: str) -> float:
    if mean_type == "average":
        sum_avr = sum(i for i in args)
        args_average = sum_avr / len(args)
        return args_average
    elif mean_type == "geometric":
        geom_val = 1
        for val in args:
            geom_val *= val
        geom_average = geom_val ** (1 / len(args))
        return geom_average


rand_args: List[int] = [randint(1, 10) for _ in range(10)]
mean_avg = "average"
mean_avg_geometric = "geometric"

print("Arithmetic mean is {}".format(avg_calc_func(*rand_args, mean_type=mean_avg)))
print("Geometric mean is {}".format(avg_calc_func(*rand_args, mean_type=mean_avg_geometric)))
