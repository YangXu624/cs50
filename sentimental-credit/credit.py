# TODO
from math import pow
from cs50 import get_int

number = 0

while number < pow(10, 12) or pow(10, 13) <= number < pow(10, 15) or number >= pow(10, 16):
    number = get_int("Number: ")

