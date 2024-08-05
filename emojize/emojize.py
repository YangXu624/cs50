import emoji

def main():
    while True:
        try:
            inp = input("Input: ").split(" ")
            for i in range(len(inp)):
                print(emoji.emojize(f"{inp[i]}", language = "alias"), end = " ")
            print("")
            return
        except EOFError:
            print("")
            break
        except IndexError:
            continue

main()
