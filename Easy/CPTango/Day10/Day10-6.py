#https://www.hackerrank.com/challenges/plus-minus/problem
import sys

pos=0
neg=0
zer=0
N=int(input())
arr=list(map(int, sys.stdin.readline().split()))

for i in arr:
    if i > 0:
        pos+=1
    elif i < 0:
        neg+=1
zer=N-pos-neg

print("{:.6f}".format(pos/N))
print("{:.6f}".format(neg/N))
print("{:.6f}".format(zer/N))
