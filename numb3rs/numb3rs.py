import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if re.search(r"^\d+\.\d+\.\d+\.\d+$", ip):
        splitted = ip.split(".")

        for num in splitted:
            if int(num) > 255:
                return False
        return True

    else:
        return False


if __name__ == "__main__":
    main()
