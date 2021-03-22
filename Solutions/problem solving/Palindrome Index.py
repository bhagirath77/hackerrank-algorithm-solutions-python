#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the 
n=int(input())
for n0 in range(n):
    s=list(input())
    if list(reversed(s))==s:
        print (-1)
    else:
        for _ in range(1,(len(s)//2)+1):
            if s[_-1]!= s[-_]:
                break
        s1=s[:]
        del s[_-1]
        del s1[-_]
        if list(reversed(s))==s:
            print (_-1)
        else:
            print (len(s)+1-_)
