import sys

n, t = map(int, sys.stdin.readline().split())
width = list(map(int, sys.stdin.readline().split()))
for i in range(t):
    a, b = map(int, sys.stdin.readline().split())
    result = min(width[a:b+1])
    print(result)
