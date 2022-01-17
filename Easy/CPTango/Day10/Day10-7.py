#https://www.hackerrank.com/challenges/staircase/problem

N=int(input())

for i in range(N-1,-1,-1):
    for j in range(i):
        print(" ",end='')
    for k in range(N-i):
        print("#",end='')
    print()
    