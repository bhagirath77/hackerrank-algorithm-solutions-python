import math
import os
import random
import re
import sys

def countingValleys(n, s):
    level = 0
    val = 0
    for  move in s:
        if move == "U":
            level += 1
            if level == 0:
                val += 1
        else:
            level -= 1
    print (val)




if __name__ == '__main__':

    n = int(input())

    s = input()

    result = countingValleys(n, s)
