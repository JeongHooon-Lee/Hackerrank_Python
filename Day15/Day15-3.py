#https://www.hackerrank.com/challenges/picking-numbers/problem?isFullScreen=true

import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
array = [ 0 for _ in range(100) ]

for i in a:
    array[i] += 1

answer=0
for i in range(99):
    if array[i]+array[i+1] > answer:
        answer = array[i]+array[i+1]
        
print(answer)