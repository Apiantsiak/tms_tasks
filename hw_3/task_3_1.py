# Insert the number. If this number is divisible by 1000 without a remainder, then display the "millennium".

user_number = int(input("Enter number: "))

if user_number % 1000 == 0:
    print("millennium")
