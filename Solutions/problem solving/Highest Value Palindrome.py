#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the highestValuePalindrome function below.
def highestValuePalindrome(strr, k):
    strr=[int(i) for i in strr]
    palin = strr[:]
    # Iinitialize l and r by leftmost and 
    # rightmost ends 
    l = 0
    r = len(strr) - 1
    # first try to make palindrome 
    while (l <= r): 
          
        # Replace left and right character by 
        # maximum of both 
        if (strr[l] != strr[r]): 
            palin[l] = palin[r] = max(strr[l], strr[r]) 
              
            # print(strr[l],strr[r]) 
            k -= 1
        l += 1
        r -= 1
    if (k < 0): 
        print(-1)
    else:
        l = 0
        r = len(strr) - 1
        while (l <= r): 
            if (l == r): 
                if (k > 0): 
                    palin[l] = 9
            if (palin[l] < 9): 
                if (k >= 2 and palin[l] == strr[l] and palin[r] == strr[r]): 
                    k -= 2
                    palin[l] = palin[r] = 9
                elif (k >= 1 and (palin[l] != strr[l] or palin[r] != strr[r])): 
                    k -= 1
                    palin[l] = palin[r] = 9
            l += 1
            r -= 1
        palin=[str(i) for i in palin]
        print(''.join(palin))         



if __name__ == '__main__':

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    s = input()

    result = highestValuePalindrome(s,k)
