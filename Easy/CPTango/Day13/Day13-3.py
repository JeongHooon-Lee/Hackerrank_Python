#https://www.hackerrank.com/challenges/migratory-birds/problem

import sys
import collections

n = int(sys.stdin.readline())
arr = [-1,0,0,0,0,0]

for i in list(map(int, sys.stdin.readline().split())):
    arr[i]+=1

print(arr.index(max(arr)))