import sys

def chocolate(m,wrappers):
    if wrappers < m:
        return 0
    return wrappers//m+chocolate(m,wrappers-wrappers//m*m+wrappers//m)

for i in range(int(input())):
    result = 0
    n, c, m = map(int, sys.stdin.readline().split())
    bars = n//c
    result = bars+chocolate(m,bars)
    print(result)
