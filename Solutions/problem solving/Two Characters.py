#!/bin/python3

import math
import os
import random
import re
import sys
def grt(s,lis):
    lo=[]
    for i in s:
        if i in lis:
            lo.append(i)
    y=0
    for i in range(len(lo)-1):
        if(lo[i]==lo[i+1]):
            y=1
            break
    if(y==0):
        return len(lo)
    else:
        return 0
    
            

# Complete the alternate function below.
def alternate(s):
    lis=list(s)
    sad=list(set(lis))
    y=0
    l=len(sad)
    for i in range(l):
        for j in range(l):
            if(i!=j):
                lis=[]
                lis.append(sad[i])
                lis.append(sad[j])
                x=grt(s,lis)
                if(x>y):
                    y=x
    print(y)
                

if __name__ == '__main__':
    l = int(input().strip())

    s = input()

    result = alternate(s)
