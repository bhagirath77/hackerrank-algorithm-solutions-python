import math
import os
import random
import re
import sys

def diagonalDifference(arr,n):
    x=0
    y=0
    for i in range(n):
        x+=arr[i][i]
    for i in range(n):
        y+=arr[i][n-i-1]
    z=abs(x-y)
    print(z)
    
    

if __name__ == '__main__':

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr,n)
