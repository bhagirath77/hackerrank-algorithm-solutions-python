#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the gemstones function below.
def gemstones(arr):
    lis=list(arr[0])
    lisa=set(lis)
    lis=list(lisa)
    lisi=[]
    for i in range(1,len(arr)):
        lise=list(arr[i])
        for j in lis:
            if(lise.count(j)==0):
                lisi.append(j)
    lin=set(lisi)
    lisi=list(lin)
    for i in lisi:
        lis.remove(i)
    print(len(lis))

if __name__ == '__main__':
    n = int(input())

    arr = []

    for _ in range(n):
        arr_item = input()
        arr.append(arr_item)

    result = gemstones(arr)
