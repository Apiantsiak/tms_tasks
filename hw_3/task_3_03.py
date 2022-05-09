# Enter a two-word sentence. Change words' places , add an exclamation mark to the beginning and to the end,
# output the final sentence on the screen.

sentence: str = input("Enter sentence: ")
split_sentence: list = sentence.split(" ")
reverse_sentence: list = sorted(split_sentence, reverse=True)

print("!{} {}!".format(reverse_sentence[0], reverse_sentence[1]))
