#https://www.hackerrank.com/challenges/angry-professor/problem?isFullScreen=true

import sys

for i in range(int(input())):
    n, k = map(int, sys.stdin.readline().split())
    times = list(map(int, sys.stdin.readline().split()))
    answer = 0
    
    for i in times:
        if i <= 0:
            answer += 1
    
    if answer >= k:
        print("NO")
    else:
        print("YES")