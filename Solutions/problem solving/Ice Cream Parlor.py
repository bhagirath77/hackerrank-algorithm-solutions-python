#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the icecreamParlor function below.
def icecreamParlor(m, arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if(i!=j and arr[i]+arr[j]==m):
                break
        if(i!=j and arr[i]+arr[j]==m):
            break
    x=i+1
    y=j+1
    print(min(x,y),max(x,y))

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        m = int(input())

        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = icecreamParlor(m, arr)
