# Ввести число, проверить на то, что было введено именно
# число. Возвести его в куб.

numb: str = input("Enter number: ")

if isinstance(int(numb), int):
    print(int(numb) ** 3)
