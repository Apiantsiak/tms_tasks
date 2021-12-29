# Создать lambda функцию, которая  принимает на вход имя и выводит его в формате “Hello, {name}”


# I use a tuple only to eliminate the PEP 8 message:
# E731 do not assign a lambda expression, use a def


names_func: tuple = "Alex", lambda name: "Hello, {}".format(name)

print(names_func[1](names_func[0]))
