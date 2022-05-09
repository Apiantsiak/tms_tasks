# Просуммировать неопределенное количество чисел,
# вводимых пользователем, суммировать до тех пор,
# пока пользователь не введёт слово «стоп»

user_numbs: list = []
numb: str = input("Enter number: ")

while True:
    user_numbs.append(int(numb))
    numb = input("Enter next number: ")
    if numb == "стоп":
        break

print("The sum of the numbers is", sum(user_numbs))
