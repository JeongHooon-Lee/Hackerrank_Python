#https://www.hackerrank.com/challenges/save-the-prisoner/problem?isFullScreen=true

import sys

for i in range(int(input())):
    n,m,s = map(int, sys.stdin.readline().split())
    
    temp = m % n
    print(s+temp-1)
    