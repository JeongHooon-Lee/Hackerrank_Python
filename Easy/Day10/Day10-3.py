#https://www.hackerrank.com/challenges/compare-the-triplets/problem
import sys

a=list(map(int, sys.stdin.readline().split()))
b=list(map(int, sys.stdin.readline().split()))

answer=[0,0]
for i in range(3):
    if a[i] > b[i]:
        answer[0]+=1
    elif a[i] < b[i]:
        answer[1]+=1

for i in answer:
    print(i, end=' ')
print()