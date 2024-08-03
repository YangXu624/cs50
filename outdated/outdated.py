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
    date = convert(get_input())
    print(date)

def get_input():
    c = 0
    while c < 2:
        date = input("Date: ")

        for i in range(len(date)):
            if date[i] == "/":
                c += 1
            elif date[i] == ",":
                c += 2
