import sys


for i in range(int(input())):
    k = int(input())
    n = int(input())
    cost = list(map(int, sys.stdin.readline().split()))
    for j in range(n):
        for m in range(j+1,n):
            if cost[j]+cost[m] == k:
                print(j+1,m+1)
                break
    

