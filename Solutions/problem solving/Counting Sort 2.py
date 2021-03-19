#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingSort function below.
def countingSort(arr):
    lis= [0] * 100
    for i in arr:
        lis[i] += 1
    for i in range(0, 100):
        for j in range(0, lis[i]):
            print(i, end=' ')
            
if __name__ == '__main__':

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)
