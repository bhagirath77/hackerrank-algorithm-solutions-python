import math
import os
import random
import re
import sys

# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):
    x=len(word)
    y=1
    for i in range(x):
        z=ord(word[i])-97
        if(y<h[z]):
            y=h[z]
    print(x*y)



if __name__ == '__main__':

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

