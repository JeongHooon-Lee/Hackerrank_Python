#https://www.hackerrank.com/challenges/drawing-book/problem?isFullScreen=true

import sys

n = int(sys.stdin.readline())
p = int(sys.stdin.readline())

if p-1 < n-p:
    if p == 1:
        return 0
    else:
        if p % 2 == 0:
            p+=1
        return (p-1)//2
else:
    if p == n:
        return 0
    else:
        if p%2 == 1:
            p-=1
        return (n-p)//2
    