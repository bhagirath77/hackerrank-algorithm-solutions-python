#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the gameOfThrones function below.
def gameOfThrones(s):
    lis=list(s)
    lis.sort()
    x=0
    i=0
    while(i<len(lis)):
        if(lis.count(lis[i])>1):
            if(lis.count(lis[i])%2!=0):
                x+=1
            i+=lis.count(lis[i])
        else:
            x+=1
            i+=1
        if(x>1):
            print("NO")
            break
    else:
        print("YES")


if __name__ == '__main__':
    s = input()

    result = gameOfThrones(s)
