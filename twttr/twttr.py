def main():
    list = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    sen = input("Input: ")

    i = 0
    while i < int(len(sen)):
        if sen[i] in list:
            sen = sen.replace(sen[i], "")
        else:
            i += 1

    print("Output:", sen)

main()
