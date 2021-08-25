#https://www.hackerrank.com/challenges/array-left-rotation/problem
import sys

A,B= map(int, sys.stdin.readline().split())

arr= list(map(int, sys.stdin.readline().rstrip().split()))

for i in range(B):
    arr.append(arr[0])
    del arr[0]
    
for i in arr:
    print(i, end=' ')