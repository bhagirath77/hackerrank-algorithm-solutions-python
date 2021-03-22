#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    x=0
    res = [s[i: j] for i in range(len(s)) 
          for j in range(i + 1, len(s) + 1)] 
    res=[list(i) for i in res]
    res=[sorted(i) for i in res]
    res=[''.join(i) for i in res]
    lai=set(res)
    for i in lai:
        if(res.count(i)>1):
            y=res.count(i)
            x+=(y*(y-1))/2
    print(int(x))


if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

