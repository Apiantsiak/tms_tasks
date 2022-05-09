# Рассчитать значение х определив и использовав необходимую функции.


def calculate_func(numb: int) -> float:
    result = ((numb ** 0.5) + numb) / 2
    return result


X = calculate_func(5) + calculate_func(12) + calculate_func(19)
print(X)
