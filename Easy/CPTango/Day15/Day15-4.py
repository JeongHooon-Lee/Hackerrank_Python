#https://www.hackerrank.com/challenges/the-hurdle-race/problem?isFullScreen=true

import sys

n, k = map(int, sys.stdin.readline().split())
height = list(map(int, sys.stdin.readline().split()))

if max(height) - k > 0:
    print(max(height)-k)
else:
    print(0)
