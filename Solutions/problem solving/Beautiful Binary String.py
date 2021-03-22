#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulBinaryString function below.
def beautifulBinaryString(b):
    x=list(b)
    z=0
    y=str(b)
    for i in range(1,len(x)-1):
        b=str(y[:])
        if(b[i-1:i+1]=='01' and b[i+1]=='0'):
            y=b[0:i+1]+'1'+b[i+2:]
            z+=1
    print(z)

if __name__ == '__main__':
    n = int(input())

    b = input()

    result = beautifulBinaryString(b)
