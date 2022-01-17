#https://www.hackerrank.com/challenges/divisible-sum-pairs/problem

import sys

n, k = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
count=0

for i in range(n):
    for j in range(i+1,n):
        if (arr[i]+arr[j]) % k == 0:
            count+=1
        
print(count)