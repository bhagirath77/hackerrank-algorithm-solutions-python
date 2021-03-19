#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the insertionSort1 function below.
def insertionSort1(n, arr):
    x=arr[-1]
    for i in range(n-2):
        if arr[n-i-2]>x:
            arr[n-i-1]= arr[n-i-2]
            print(*arr, sep=' ')
        else:
            arr[n-i-1] = x
            print(*arr, sep=' ') 
            break
    if arr[1] > x:
        if arr[0] >x:
            arr[1] = arr[0]
            print(*arr, sep=' ')
            arr[0]=x
            print(*arr, sep=' ')
        else:
            arr[1] = x
            print(*arr, sep=' ')

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
