# TODO
from cs50 import get_int
import re
import sys


credit = input("Card Number: ")
list = re.findall("\d", credit)

if len(list) >0:
    i = 0
    count = 0
    for (i) in list[0::2]:
        mul = int(i)* 2
        if mul > 9:
            n9 = int(repr(mul)[-1])
            n8 = int(repr(mul)[-2])
            mul = n9 + n8
        count += mul
    for i in list[1::2]:
        mult = int(i)
        count += mult
    print(count)


