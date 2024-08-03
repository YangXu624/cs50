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
    while True:
        try:
            date = input("Date: ")
