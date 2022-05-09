# Ввести два целых числа A и B ( A < B ).
# Вывести в порядке возрастания все целые числа,
# расположенные между A и B (включая сами числа A и B ),
# а также количество N этих чисел. [01-08-For2]

a: int = int(input("Enter A: "))
b: int = int(input("Enter B: "))

for var in range(a, b + 1):
    print(var)

print(len(range(a, b + 1)))
