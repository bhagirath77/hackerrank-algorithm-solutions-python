#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isValid function below.
def isValid(s):
    s=list(s)
    lis=[]
    l=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for i in l:
        if(s.count(i)>0):
            lis.append(s.count(i))
    li=set(lis)
    x=0
    if(len(li)>2):
        print("NO")
    else:
        for i in li:
            if(lis.count(i)>1):
                x+=1
            if(lis.count(i)==1 and i-1 not in li):
                if(i!=1):
                    x+=1
            if(x>1):
                print("NO")
                break
        else:
            print("YES")
if __name__ == '__main__':
    s = input()

    result = isValid(s)
