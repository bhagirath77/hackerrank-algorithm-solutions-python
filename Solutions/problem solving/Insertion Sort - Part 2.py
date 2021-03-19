#!/bin/python3

import math
import os
import random
import re
import sys

def doSort(arr,i):
    x=sorted(arr[:i+1])+arr[i+1:]
    return ' '.join(str(k) for k in x)
# Complete the insertionSort2 function below.
def insertionSort2(n, arr):
    for i in range(1,n):
        print(doSort(arr,i))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
