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
    while True:
        try:
            date = get_input()
            break
        except TypeError:
            return

    if len(date) == 3:
        for i in range(3):
            if date[0] in months:
                mth = "%02d" % (int(months.index(date[0])) + 1)
                day = "%02d" % int(date[1])
                print(f"{date[2]}-{mth}-{day}")
            else:
                mth = "%02d" % int(date[0])
                day = "%02d" % int(date[1])
                print(f"{date[2]}-{mth}-{day}")
            return
    else:
        print("")
        return

def get_input():
    c = 0
    while c < 2:
        try:
            date = input("Date: ")
        except EOFError:
            empty_list = ['0']
            return empty_list

        for i in range(len(date)):
            if date[i] == "/":
                c += 1
            elif date[i] == ",":
                c += 5

        ## c = 2 means date is in MM/DD/YYYY form, while c = 5 means date in Month Day, Year form
        if c == 2:
            numbers = date.split("/")
            if int(numbers[1]) > 31 or int(numbers[1]) < 1:
                c = 0
            else:
                return numbers
        elif c == 5:
            words = date.split(" ")
            for i in range(len(words)):
                if words[i] in months:
                    words[1] = words[1].strip(",")
                    if int(words[1]) > 31 or int(words[1]) < 1:
                        c = 0
                    else:
                        return words
                else:
                    c = 0
        ## c reset to 0 to restart while loop
        else:
            c = 0

main()
