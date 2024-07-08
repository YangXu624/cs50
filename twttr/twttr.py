def main():
    list = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    sen = input("Input: ")

    for i in range(len(sen)):
        if sen[i] in list:
            sen = sen.replace(sen[i], "")

    print("Output:", sen)

main()
