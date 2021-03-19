import sys


n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
x = [int(x_temp) for x_temp in input().strip().split(' ')]

x = sorted(x)

count_trans = 0
last = x[0]
i = 0
while(i < n):
    count_trans = count_trans + 1
    next_point = x[i] + k
    while(i < n and x[i] <= next_point):
        i = i + 1
    next_point = x[i-1] + k
    while(i < n and x[i] <= next_point):
        i = i + 1

print(count_trans)
