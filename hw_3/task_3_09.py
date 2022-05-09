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

from math import sqrt


a: float = float(input("Enter a: "))
b: float = float(input("Enter b: "))
c: float = float(input("Enter c: "))

D: float = b ** 2 - 4 * a * c

print("Дискриминант D = {}".format(D))

if D > 0:
    x1 = (-b + sqrt(D)) / (2 * a)
    x2 = (-b - sqrt(D)) / (2 * a)
    print("x1 = {} , x2 = {}".format(x1, x2))
elif D == 0:
    x = -b / (2 * a)
    print("x = {}".format(x))
else:
    print("Корней нет")
