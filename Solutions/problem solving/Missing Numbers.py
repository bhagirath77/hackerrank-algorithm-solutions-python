#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the missingNumbers function below.
def missingNumbers(arr, brr):
    x=[]
    brr.sort()
    i=0
    while(i<len(brr)):
        if(brr.count(brr[i])!=arr.count(brr[i])):
            x.append(brr[i])
        i=i+brr.count(brr[i])
    
    x=set(x)
    x=list(x)
    x.sort()
    print(*x)



if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    m = int(input())

    brr = list(map(int, input().rstrip().split()))

    result = missingNumbers(arr, brr)
