# Create two lists of arbitrary content.
# Add to each list one element at the end and at the beginning.
# Extend the first list with the second.
# Display all changes on the screen.


names = ["Bob", "Stan", "Mike"]
numbers = [22, 34, 15]
names.append("Tony")
numbers.append(28)


print(names)
print(numbers)


names.insert(0, "Bil")
numbers.insert(0, 13)


print(names)
print(numbers)


names.extend(numbers)


print(names)
