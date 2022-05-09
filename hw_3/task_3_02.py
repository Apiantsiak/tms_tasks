# Ask user enter for two integers. Output a line like “2 plus 3 equals 5”.

first_numb, second_numb = int(input("Enter first number: ")), int(input("Enter second number: "))
numbers_sum = first_numb + second_numb

print("{} plus {} equals {}".format(first_numb, second_numb, numbers_sum))
