#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the marsExploration function below.
def marsExploration(s):
    x=len(s)
    y=int(x/3)
    z=['S','O','S']*y
    lis=list(s)
    c=0
    for i in range(x):
        if(z[i]!=lis[i]):
            c+=1
    print(c)

if __name__ == '__main__':

    s = input()

    result = marsExploration(s)
