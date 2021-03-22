#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the anagram function below.
def anagram(s):
    x=len(s)
    if(x%2==0):
        z=0
        lis=[None]*int(x/2)
        for i in range(int(x/2)):
            lis[i]=s[i]
        for i in range(int(x/2),x):
            if s[i] in lis:
                lis.remove(s[i])
            else:
                z+=1
        print(z)

    else:
        print(-1)


if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        s = input()

        result = anagram(s)
