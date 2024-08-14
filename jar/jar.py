from sys import exit

class Jar:
    def __init__(self, capacity=12, size=0):
        self.capacity = capacity
        self.size = size

    def __str__(self):
        cookie_string = []
        for i in range(self.capacity):
            cookie_string.append("🍪")
        return f"{cookie_string}"


    def deposit(self, n):
        self.size += int(n)
        if self.size > self.capacity:
            raise ValueError("Cookies exceed jar size!!")

    def withdraw(self, n):
        self.size = self.size - int(n)
        if self.size < 0:
            raise ValueError("Cookies fall below zero!!")


    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, cap):
        if int(cap) < 0:
            raise ValueError("Capacity cannot be negative!!")
        try:
            self._capacity = int(cap)
            return self._capacity
        except ValueError:
            raise ValueError("Capacity not integer")


    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, ck):
        self._size = int(ck)

def main():
    jar = Jar()
    while True:
        try:
            jar.deposit(input("Deposit: "))
            jar.withdraw(input("Withdraw: "))
        except EOFError:
            print("")
            print(jar)
            return

if __name__ == "__main__":
    main()
