#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hackerrankInString function below.
def hackerrankInString(s):
    x=list(s)
    st='hackerrank'
    y=list(st)
    j=0
    z=0
    for i in range(len(s)):
        if(x[i]==y[j]):
            j+=1
            z+=1
        if(z==10):
            print("YES")
            break
    else:
        print("NO")


if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)

