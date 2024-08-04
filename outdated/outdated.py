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
    while True:
        try:
            date = input("Date: ").strip()

            for i in range(len(date)):
                if date[i] == "/":
                    numbers = date.split("/")
                    if int(numbers[0]) > 0 and int(numbers[0]) < 13 and int(numbers[1]) > 0 and int(numbers[1]) < 32 and int(numbers[2]) > 0:
                        return numbers

                elif date[i] == ",":
                    chars = date.split()
                    if chars[0] in months:
                        chars[1] = chars[1].replace(",", "")
                        if int(chars[1]) > 0 and int(chars[1]) < 32 and int(chars[2]) > 0:
                            return chars

        except EOFError:
            break
        except ValueError:
            continue

main()
