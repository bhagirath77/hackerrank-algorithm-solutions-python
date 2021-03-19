#!/bin/python3

import math
import os
import random
import re
import sys
import functools

# Complete the balancedSums function below.
def balancedSums(arr):
    total = sum(arr)
    x= 0
    for i in arr:
        if total - i == 2*x:
            print('YES')
            break
        else:
            x += i
    else:
        print('NO')



if __name__ == '__main__':
    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = balancedSums(arr)
