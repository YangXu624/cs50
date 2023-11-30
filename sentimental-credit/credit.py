# TODO
from math import pow
from cs50 import get_int

number = get_int("Number: ")

if number < pow(10, 12) or pow(10, 13) <= number < pow(10, 14) or number >= pow(10, 16):
    print("INVALID")

else:
    odd_sum = 0
    for i in range(8):
        odd_sum += (number % pow(10, 2 * i + 1) - number % pow(10, 2 * i)) / pow(10, 2 * i)

    even_sum = 0
    for i in range(8):
        x = 2 * (number % pow(10, 2 * i + 2) - number % pow(10, 2 * i + 1)) / pow(10, 2 * i + 1)
        if x > 9:
            even_sum += x % 10 + (x - x % 10) / 10
        else:
            even_sum += x

    final_num = even_sum + odd_sum

    if final_num % 10 == 0:
        if len(f"{number}") == 13:
            if (number - number % pow(10, 12)) / pow(10, 12) == 4:
                print("VISA")
        if len(f"{number}") == 15:
            if (number - number % pow(10, 13)) / pow(10, 13) == 34 or (number - number % pow(10, 13)) / pow(10, 13) == 37:
                print("AMEX")
        if len(f"{number}") == 16:
            if (number - number % pow(10, 15)) / pow(10, 15) == 4:
                print("VISA")
            elif 50 < (number - number % pow(10, 14)) / pow(10, 14) < 56:
                print("MASTERCARD")

    print("INVALID")
