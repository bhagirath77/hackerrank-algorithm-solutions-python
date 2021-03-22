#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the funnyString function below.
def funnyString(s):
    y=[0]*(len(s)-1)
    for i in range(len(s)-1):
        y[i]=abs(ord(s[i+1])-ord(s[i]))
    x=int(len(s)/2)
    for i in range(x):
        if(y[i]!=y[len(s)-2-i]):
            print("Not Funny")
            break
    else:
        print("Funny")


if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)
