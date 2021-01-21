import os
import sys

def timeConversion(s):
    x=int(s[:2])
    y=''
    if(s[-2:]=="AM"):
        if(x==12):
            x="00"
            y=x+s[2:-2]
        else:
            y=s[:-2]
    else:
        if(x==12):
              y=s[:-2]
        else:
            x+=12
            y=str(x)+s[2:-2]
        
    print(y)

        
    


if __name__ == '__main__':

    s = input()

    result = timeConversion(s)
