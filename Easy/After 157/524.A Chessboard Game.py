import sys

t = int(input())
for i in range(t):
    n,m = map(int, sys.stdin.readline().split())

    n=n%4 
    m=m%4
    if (n==0)or (n==3) or (m==0)or (m==3) :
        print("First")
    else:
        print("Second")

