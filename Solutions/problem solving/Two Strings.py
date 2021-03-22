#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the twoStrings function below.
def twoStrings(s1, s2):
    lis=list(s1)
    lisa=list(s2)
    alpha=['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
    for i in alpha:
        if lisa.count(i)!=0 and lis.count(i)!=0:
            print("YES")
            break
    else:
        print("NO")

if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)
