# TODO
from cs50 import get_int


while True:
    height = get_int("Height: ")
    if height > 0 and height < 9:
        break

for i in range(height):
    for j in range(height + i + 3):
        if j == height or j == height + 1 or i + j < height - 1:
            print(" ", end="")
        else:
            print("#", end="")

    print("")

