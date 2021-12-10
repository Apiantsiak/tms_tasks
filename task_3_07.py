# Enter a string from the keyboard.
# If the line length is more than 5 - display the value on the screen.
# If the length of the line is less than 5 - output the line “Need more!”.
# If the length of the line is 5, output the line “It is five”.

user_sentence: str = input("Enter your sentence: ")
sentence_length: int = len(user_sentence)

if sentence_length == 5:
    print("It is five")
elif sentence_length > 5:
    print("Sentence length is {}".format(sentence_length))
else:
    print("Need more!")
