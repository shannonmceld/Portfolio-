# demonstrate while loop

"""i = 0
while i < 3:
    print("meow")
    i += 1"""

# Better design

"""for i in range(3):
    print("meow")"""

# Abstraction with parameterization

def main():
    meow(3)

# Meow some number of times
def meow(n):
    for i in range(n):
        print("meow")


main()



# Prints a column of bricks, using a helper function to get input

"""from cs50 import get_int


def main():
    height = get_height()
    for i in range(height):
        print("#")


def get_height():
    while True:
        n = get_int("Height: ")
        if n > 0:
            return n


main()"""



# Prints a column of bricks, catching exceptions

def main():
    height = get_height()
    for i in range(height):
        print("#")


def get_height():
    while True:
        try:
            n = int(input("Height: "))
            if n > 0:
                return n
        except ValueError:
            print("Not an integer")


main()


"""# Prints a row of 4 question marks with a loop

for i in range(4):
    print("?", end="")
print()"""


print("?" * 4)


# Prints a 3-by-3 grid of bricks with loops

for i in range(3):
    for j in range(i+1):
        print("#", end="")
    print()