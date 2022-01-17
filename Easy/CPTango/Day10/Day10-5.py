#https://www.hackerrank.com/challenges/diagonal-difference/problem

import sys
n=int(sys.stdin.readline())

arr=[ [] for _ in range(n) ]
a=0
b=0

for i in range(n):
    tmp=list(map(int, sys.stdin.readline().split()))
    b+=tmp[n-1-i]
    a+=tmp[i]
print(abs(a-b))
