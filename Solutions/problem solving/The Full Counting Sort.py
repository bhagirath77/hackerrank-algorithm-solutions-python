#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSort function below.
def countSort(arr):
    x=int(len(arr)/2)
    for i in range(x):
        arr[i][1]='-'
    y=max(arr)
    z=int(y[0])+1
    lis=['']*z
    for i in range(2*x):
        y=int(arr[i][0])
        lis[y]+=arr[i][1]
        lis[y]+=' '
    print(''.join(lis))

if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)
