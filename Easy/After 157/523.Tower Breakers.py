import sys

t = int(input())
for i in range(t):
    n,m = map(int, sys.stdin.readline().split())
    
    if m ==1 or n%2 == 0:
        print(2)
    else:
        print(1)

