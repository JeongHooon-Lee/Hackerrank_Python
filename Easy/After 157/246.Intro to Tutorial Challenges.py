import sys

V = int(input())
n = int(input())
arr = list(map(int, sys.stdin.readline().split()))

print(arr.index(V))