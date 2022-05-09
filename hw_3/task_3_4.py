# Enter a string. Display the letter in the middle of these strings.
# Also, if this center letter is equal to the first letter in the line, then create and
# print the part of the string between the first and last characters of the original string.

user_text: str = input("Enter some text: ")
middle_letter: str = user_text[int(len(user_text) / 2)]

print(middle_letter)

if middle_letter == user_text[0].lower():
    print(user_text[1: len(user_text) - 1])
