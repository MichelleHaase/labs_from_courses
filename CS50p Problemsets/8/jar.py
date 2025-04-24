class Jar:
    def __init__(self, capacity=12, size=0):
        self._capacity = capacity
        if not type(self._capacity) == int or self._capacity < 0:
            raise ValueError("capacity needs to be a positive whole number")
        self._size = size


    def __str__(self):
        return "🍪" * self._size

    def deposit(self, n):
        if self._size + n > self.capacity:
            raise ValueError("The Jar is too small for so much Cookies")
        self._size += n

    def withdraw(self, n):
        if self._size - n < 0:
            raise ValueError("There aren't that many Cookies in the Jar")
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

