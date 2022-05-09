# Enter a string. If the string length is more than 10 characters, then create a new string with 3 exclamation marks
# at the end ('!!!') and display it. If less than 10, then display the second character of the string

user_text: str = input("Enter some text: ")

if 10 <= len(user_text):
    print("{}!!!".format(user_text))
elif len(user_text) < 10:
    print(user_text[1])
