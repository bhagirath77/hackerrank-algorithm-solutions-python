#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the quickSort function below.
def quickSort(arr):
    x=arr[0]
    y=len(arr)
    left=[]
    right=[]
    mid=[x]
    lis=[]
    for i in range(1,y):
        if(arr[i]<x):
            left.append(arr[i])
        elif(arr[i]>x):
            right.append(arr[i])
        else:
            mid.append(arr[i])
    lis=left[:]+mid[:]+right[:]
    print(*lis,sep=' ')

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = quickSort(arr)
