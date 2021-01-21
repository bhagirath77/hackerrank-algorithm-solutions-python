import math
import os
import random
import re
import sys

def aVeryBigSum(ar):
    x=0
    for i in range(len(ar)):
        x+=ar[i]
    print(x)



if __name__ == '__main__':

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(ar)

