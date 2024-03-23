# addition with int [using get_int]

"""from cs50 import get_int

# Prompt user for x
x = get_int("x: ")

# Prompt user for y
y = get_int("y: ")

# Perform addition
print (x + y)""" # Training wheels


# Addition with int [using input]

#Prompt user for x
"""x = int(input("x: "))

# Prompt user for y
y = int(input("y: "))

# Perform addition
print (x + y)"""


# Floating-point imprecision

# Prompt user for x
x = int(input("x: "))

# Prompt user for y
y = int(input("y: "))

# Divide x by y
z = x / y
print(f"{z:.50f}")
