#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the makingAnagrams function below.
def makingAnagrams(s1, s2):
    lis=list(s1)
    z=0
    for i in range(len(s2)):
        if s2[i] in lis:
            lis.remove(s2[i])
            z+=1
    print(len(s1)+len(s2)-(2*z))


if __name__ == '__main__':
    s1 = input()

    s2 = input()

    result = makingAnagrams(s1, s2)
