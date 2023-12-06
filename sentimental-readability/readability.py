from cs50 import get_string

text = get_string("Text: ")
letters = 0
words = 1
sentences = 0


for i in range(len(text)):
    if text[i] == " ":
        words += 1

    if ord(text[i]) in [33, 46, 63]:
        sentences += 1

    if 64 < ord(text[i]) < 91 or 96 < ord(text[i]) < 123:
        letters += 1

L = letters / words * 100
S = sentences / words * 100

index = 0.0588 * L - 0.296 * S - 15.8
x = round(index)

if x < 1:
    print("Before Grade 1")
elif x > 15:
    print("Grade 16+")
else:
    print(f"Grade {x}")
