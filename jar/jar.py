class Jar:
    def __init__(self, capacity=12, cookies=0):
        self.capacity = capacity
        self.cookies = cookies

    def __str__(self):
        return f"Capacity is {self.capacity}"

    def deposit(self, n):
        if n > (self.capacity - self.cookies):
            self.cookies += n
        else:
            

    def withdraw(self, n):
        ...

    @property
    def capacity(self):
        ...

    @property
    def size(self):
        ...
