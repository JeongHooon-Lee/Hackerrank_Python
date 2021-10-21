#https://www.hackerrank.com/challenges/electronics-shop/problem?isFullScreen=true

import sys

b,n,m = map(int, sys.stdin.readline().split())
keyboard = list(map(int, sys.stdin.readline().split()))
drives = list(map(int, sys.stdin.readline().split()))

answer = -1
for i in keyboard:
    for j in drives:
        if i+j <= b and i+j >= answer:
            answer = i+j
print(answer)