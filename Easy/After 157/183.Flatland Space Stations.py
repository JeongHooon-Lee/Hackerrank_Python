import sys

n, m = map(int, sys.stdin.readline().split())
c = list(map(int, sys.stdin.readline().split()))
c.sort()
result = c[0]

for i in range(1, len(c)):
    result = max(result, (c[i] - c[i-1])//2)

result = max(result, n-1 - c[-1])
print(result)