#https://www.hackerrank.com/challenges/mini-max-sum/problem

import sys

a = list(map(int, sys.stdin.readline().split()))
array = [ sum(a) for _ in range(5) ]

for i in range(len(a)):
    array[i] = array[i] - a[i]


print(min(array),max(array))
