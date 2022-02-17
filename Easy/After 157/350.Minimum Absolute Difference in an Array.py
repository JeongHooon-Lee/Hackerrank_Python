from itertools import combinations
import sys

n = int(input())
arr = list(map(int, sys.stdin.readline().split()))
arr =sorted(arr)
temp = abs(arr[1]-arr[0])
for a, b in zip(arr[:-1], arr[1:]):
    if abs(a-b) < temp:
        temp = abs(a-b)
print(temp)