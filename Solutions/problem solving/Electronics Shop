import os
import sys


def getMoneySpent(keyboards, drives, b):
    x=len(keyboards)
    y=len(drives)
    z=x*y
    lis=[-1]*z
    a=0
    for i in keyboards:
        for j in drives:
            if(i+j<=b):
                lis[a]=i+j
                a+=1
    print(max(lis))


if __name__ == '__main__':

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    moneySpent = getMoneySpent(keyboards, drives, b)

