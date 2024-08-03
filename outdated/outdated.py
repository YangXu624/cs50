def main():
    date = convert(get_input())
    print(date)

def get_input():
    while True:
        try:
            date = input("Date: ")
