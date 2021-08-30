#https://www.hackerrank.com/challenges/maximum-element/problem
#!/bin/python3
import sys

n = int(input().strip())

ops = [0]

for _ in range(n):
    nums = list(map(int, sys.stdin.readline().split()))
    if nums[0] == 1:
        ops.append( max( nums[1], ops[-1] ))
    elif nums[0] == 2:
        ops.pop()
    else:
        print(ops[-1])
        