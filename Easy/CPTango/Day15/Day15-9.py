#https://www.hackerrank.com/challenges/strange-advertising/problem?isFullScreen=true

import sys

n = int(sys.stdin.readline())

shared=5
liked=0
cumulative=0

for i in range(n):
    liked = shared//2
    cumulative+=liked
    shared = liked *3
    
print(cumulative)