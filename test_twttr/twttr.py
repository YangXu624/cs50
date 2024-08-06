list = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

def main():
    sen = input("Input: ")
    sentence = shorten(sen)
    print("Output:", sentence)


def shorten(word):
    i = 0
    while i < int(len(word)):
        if word[i] in list:
            word = word.replace(word[i], "")
        else:
            i += 1
    return word


if __name__ == "__main__":
    main()
