from sys import exit

class Jar:
    def __init__(self, capacity=12, cookies=0):
        self.capacity = capacity
        self.cookies = cookies

    def __str__(self):
        return f"Capacity is {self.capacity}"


    def deposit(self, n):
        self.cookies += int(n)
        if self.cookies > self.capacity:
            raise ValueError("Cookies exceed jar size!!")

    def withdraw(self, n):
        self.cookies = self.cookies - int(n)
        if self.cookies < 0:
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
    def cookies(self):
        return self._cookies

    @cookies.setter
    def cookies(self, ck):
        self._cookies = int(ck)

def main():
    jar = Jar()
    while True:
        try:
            jar.deposit(input("Deposit: "))
            jar.withdraw(input("Withdraw: "))
        except EOFError:
            print("")
            print(jar.cookies)
            return

if __name__ == "__main__":
    main()
