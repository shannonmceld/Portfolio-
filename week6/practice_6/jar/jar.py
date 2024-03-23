def main():
    jar = Jar()
    print(str(jar._capacity))
    print(str(jar.size))
    jar.deposit(13)
    print(str(jar))
    jar.withdraw(0)
    print(str(jar.size))
    print(str(jar))


class Jar:
    def __init__(self, capacity=12):
        self._capacity = capacity = 12
        if self._capacity < 0:
            raise ValueError ('increase value')
        self._size = 0

    def __str__(self):
        return "🍪" * self._size

    def deposit(self, n):
        self._size += n
        if self._size > self._capacity:
            raise ValueError ("passed capacity")

    def withdraw(self, n):
        self._size -= n
        if self._size < 0:
            raise ValueError ("not enough dough")


    @property
    def capacity(self):
        return self._capacity


    @property
    def size(self):
        return self._size


main()