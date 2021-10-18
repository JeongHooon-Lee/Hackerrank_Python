#https://www.hackerrank.com/challenges/sock-merchant/problem?isFullScreen=true
import sys

n = int(sys.stdin.readline())
ar = list(map(int, sys.stdin.readline().split()))

count = 0
for i in range(len(ar)):
    if ar[i] == -1:
        continue
    for j in range(i+1,len(ar)):
        if ar[i] == ar[j]:
            ar[j] = -1
            count += 1
            break

print(count)
