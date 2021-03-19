#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the runningTime function below.
def runningTime(l):
    z=0
    for i in range(1, len(l)):
        j = i-1
        key = l[j+1]
        while (j >= 0) and (l[j] > key):
           l[j+1] = l[j]
           j -= 1
           z+=1
        l[j+1] = key
    print(z)


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = runningTime(arr)
