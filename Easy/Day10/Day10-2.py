#https://www.hackerrank.com/challenges/simple-array-sum/problem
import sys

sum=0
n= input()
tmp = list(map(int, sys.stdin.readline().split()))

for i in tmp:
    sum += i 

print(sum)