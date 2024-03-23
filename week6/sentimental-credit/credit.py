# TODO
import re
import sys


# prompt for input...loop untilinput is valid
while True:
    credit = input("Card Number: ")
    list = re.findall("\d", credit)
    if credit.isdigit() and 1 < len(credit):
        break
    else:
        print("INVALID")
# make sure input is the correct length
if len(credit) < 13 or 16 < len(credit):
    print("INVALID")
    sys.exit(0)

# loop through the list and calculate checksum
elif len(credit) == 16:
    count = 0
    for i in list[0::2]:
        mul = int(i) * 2
        if mul > 9:
            a = int(repr(mul)[-1])
            b = int(repr(mul)[-2])
            mul = a + b
        count += mul
    for i in list[1::2]:
        mult = int(i)
        count += mult
# loop through the list and calculate checksum
elif len(credit) == 15 or 13 == len(credit):
    count = 0
    for i in list[1::2]:
        mul = int(i) * 2
        if mul > 9:
            a = int(repr(mul)[-1])
            b = int(repr(mul)[-2])
            mul = a + b
        count += mul
    for i in list[0::2]:
        mult = int(i)
        count += mult

# get remainer of checksum
check_sum = count % 10

# print the card that matches lughn algorithm
if check_sum == 0:
    list_index0 = int(list[0])
    list_index1 = int(list[1])
    if list_index0 == 3 and list_index1 == 4 or list_index1 == 7:
        print("AMEX")
    elif list_index0 == 5 and 1 <= list_index1 <= 5:
        print("MASTERCARD")
    elif list_index0 == 4:
        print("VISA")
    # ant print the one that do not match lughn algorithm
    else:
        print("INVALID")
else:
    print("INVALID")

