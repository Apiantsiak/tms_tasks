# Ask the user for age. If age is less than 0 - display Incorrect input,
# if less than 18 - display CocaCola, otherwise - display Beer.

age: int = int(input("Enter your age: "))

if age <= 0:
    print("Wrong input")
elif age < 18:
    print("CocaCola")
else:
    print("Beer")
    