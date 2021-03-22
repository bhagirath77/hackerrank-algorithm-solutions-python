#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the theLoveLetterMystery function below.
def theLoveLetterMystery(s):
    lis=list(s)
    x=len(lis)
    z=0
    #if(x%2!=0):
     #   for i in range(int((x-1)/2)):
      #      z+=abs(ord(lis[i])-ord(lis[x-1-i]))
    #else:
    for i in range(int(x/2)):
            z+=abs(ord(lis[i])-ord(lis[x-1-i]))
    print(z)

if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        s = input()

        result = theLoveLetterMystery(s)

