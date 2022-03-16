# Ex.1 Loops
# Написать цикл, который опрашивает пользователя и
# выводит рандомное число.
# Цикл должен прерываться по символу Q(q)


from random import randint


while True:

    print("Do you need a randon number from 1 to 100?")
    user_choice = input("If you need a number enter 'Y/y' or enter 'Q/q' to exit: ").lower()

    give_numb = user_choice == "y"
    exit_loop = user_choice == "q"

    if give_numb:
        print(f"\nThis is your random number: {randint(1, 100)}\n")
    elif exit_loop:
        print("\nBye\n")
        break
