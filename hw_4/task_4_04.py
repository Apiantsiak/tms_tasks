# Ввести с клавиатуры целое число n.
# Получить сумму кубов всех целых чисел от 1 до n(включая n) используя цикл while

numb: int = int(input("Enter number: "))
cube_sum: int = 0

while numb:
    cube_sum += numb ** 3
    numb -= 1

print(cube_sum)
