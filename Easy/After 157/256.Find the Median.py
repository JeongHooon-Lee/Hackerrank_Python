import sys

n = int(input())
arr = list(map(int, sys.stdin.readline().split()))
arr = sorted(arr)
print(arr[n//2])