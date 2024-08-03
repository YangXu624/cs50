months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():
    date = get_input()
    print(date)
    return

def get_input():
    c = 0
    while c < 2:
        try:
            date = input("Date: ")
        except EOFError:
            break

        for i in range(len(date)):
            if date[i] == "/":
                c += 1
            elif date[i] == ",":
                c += 5

        ## c = 2 means date is in MM/DD/YYYY form, while c = 5 means date in Month Day, Year form
        if c == 2:
            numbers = date.split("/")
            if numbers[1] > 31 or numbers[1] < 1:
                c = 0
            else:
                return numbers
        elif c == 5:
            words = date.split(" ")
            for i in range(len(words)):
                if words[i] in months:
                    return words
                else:
                    c = 0
        ## c reset to 0 to restart while loop
        else:
            c = 0

main()
