from cs50 import get_string

text = get_string("Text: ")
letters = 0
words = 1
sentences = 0


for i in range(len(text)):
    if text[i] == " ":
        words += 1

    if ord(text[i]) == 33 or 46 or 63:
        sentences += 1

    if 64 < ord(text[i]) < 91 or 96 < ord(text[i]) < 123:
        letters += 1

print(letters, words, sentences)

