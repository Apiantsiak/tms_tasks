# Enter a sentence. If the number of characters in the sentence is a multiple of 3 - add "!" to the end of the line.
# Display the string on the screen.

sentence: str = input("Enter your sentence: ")

if len(sentence) % 3 == 0:
    print(sentence + "!")
else:
    print(sentence)
