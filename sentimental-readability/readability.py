from cs50 import get_string

text = get_string("Text: ")
words = 1
sentences = 0


for i in range(len(text))
    if text[i] == " "
        words += 1

    if text[i] == "." or "?" or "!"
        sentences += 1

