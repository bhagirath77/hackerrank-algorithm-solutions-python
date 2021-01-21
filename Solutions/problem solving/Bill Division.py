import math
import os
import random
import re
import sys

def bonAppetit(bill, k, b):
    x=0
    for i in range(len(bill)):
        if(i!=k):
            x+=bill[i]
    x=int(x/2)
    if(x==b):
        print("Bon Appetit")
    else:
        print(b-x)


if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
