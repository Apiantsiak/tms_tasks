# Enter a sentence. If there is a word "code" in the sentence - display Yes, otherwise display No.

sentence: str = input("Enter your sentence: ")
sub_string: str = "code"

if sub_string in sentence.lower():
    print("YES")
else:
    print("NO")
