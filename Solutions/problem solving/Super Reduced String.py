#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the superReducedString function below.
def superReducedString(s):
    st=list(s)
    str=[]
    m=0
    for i in range(len(st)-1):
            if(st[i]==st[i+1] and st[i]!=' '):
                st[i]=' '
                st[i+1]=' '
                m=+1
    for i in st:
            if(i!=' '):
                str.append(i)
    s=''.join(str)
    if(m!=0):
        superReducedString(s)
    else:  
        if(len(str)!=0):
            print(''.join(str))   
        else:
            print("Empty String")



if __name__ == '__main__':

    s = input()

    result = superReducedString(s)

