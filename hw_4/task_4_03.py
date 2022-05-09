# Просуммировать неопределенное количество чисел, вводимых пользователем, суммировать до тех пор,
# пока пользователь не введёт слово «стоп».
# Не учитывать числа кратные 5


user_numbs: list = []
numb: str = input("Enter number: ")

while True:
    if numb == "стоп":
        break
    elif int(numb) % 5 == 0:
        numb = input("Enter next number: ")
        continue
    user_numbs.append(int(numb))
    numb = input("Enter next number: ")

print("The sum of the numbers is", sum(user_numbs))
