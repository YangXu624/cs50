#First attempt before I found the 'replace' function
def main1():
    line = input()

    words = line.split(" ")

    for i in range (len(words)):
        print(words[i], end = "")
        print("...", end = "")

    print()

#Second attempt after I found the 'replace' function
def main2():
    line = input().replace(" ", "...")

    print(line)

main2()
