# Написать программу, в которой вводятся два операнда Х и Y и знак операции sign (+, –, /, *).
# Вычислить результат Z в зависимости от знака.
# Предусмотреть реакции на возможный неверный знак операции, а также на ввод Y=0 при делении.
# Организовать возможность многократных вычислений без перезагрузки программа (т.е. построить бесконечный цикл).
# В качестве символа прекращения вычислений принять ‘0’ (т.е. sign='0').

from random import randint, choice

X: int = randint(-100, 100)
Y: int = randint(-100, 100)
sign_ls = ["+",
           "-",
           "/",
           "*",
           "0",
           ]

user_sign: str = choice(sign_ls)

while True:
    X: int = randint(-100, 100)
    Y: int = randint(-100, 100)
    user_sign: str = choice(sign_ls)
    if Y == 0 and user_sign == "/" or user_sign not in sign_ls:
        print("Error")
    elif user_sign == "0":
        print(f"Enter sign: {user_sign}\nExit")
        break
    else:
        print(f"Enter X: {str(X)}\nEnter Y: {str(Y)}\nEnter sign: {user_sign}")
        if user_sign == "+":
            print("Z =", X+Y)
        elif user_sign == "-":
            print("Z =", X-Y)
        elif user_sign == "/":
            print("Z =", X/Y)
        elif user_sign == "*":
            print("Z =", X*Y)
