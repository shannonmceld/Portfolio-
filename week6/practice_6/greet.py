# Uppercases string one character at a time

"""before = input("Before: ")
print("After:  ", end="")
for c in before:
    print(c.upper(), end="")
print()"""



# Printing command-line arguments, indexing into argv

"""from sys import argv

for i in range(len(argv)):
    print(argv[i])"""

# Printing command-line arguments using a slice

from sys import argv

for arg in argv[1:]:
    print(arg)


# Exits with explicit value, importing sys

"""import sys

if len(sys.argv) != 2:
    print("Missing command-line argument")
    sys.exit(1)

print(f"hello, {sys.argv[1]}")
sys.exit(0)"""