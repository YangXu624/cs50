from sys import exit

class Jar:
    def __init__(self, capacity=12, cookies=0):
        self.capacity = capacity
        self.cookies = cookies

    def __str__(self):
        return f"Capacity is {self.capacity}"


    def deposit(self, n):
        self.cookies += int(n)
        print(self.cookies)

    def withdraw(self, n):
        self.cookies = self.cookies - int(n)
        print(self.cookies)


    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, cap):
        try:
            self._capacity = int(cap)
            return self._capacity
        except ValueError:
            exit("Capacity not integer")


    @property
    def cookies(self):
        return self._cookies

    @cookies.setter
    def cookies(self, ck):
        if int(ck) < 0 or int(ck) > self._capacity:
            exit("Not possible to withdraw/deposit!!")
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
