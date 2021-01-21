import math
import os
import random
import re
import sys

def plusMinus(arr,n):
    x=0
    y=0
    z=0
    for i in range(n):
        if(arr[i]>0):
            x+=1
        elif(arr[i]<0):
            y+=1
        else:
            z+=1
    print("{:.6f}".format(x/n))
    print("{:.6f}".format(y/n))
    print("{:.6f}".format(z/n))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr,n)
