#https://www.hackerrank.com/challenges/apple-and-orange/problem
import sys

s,t = map(int, sys.stdin.readline().split())
a,b = map(int, sys.stdin.readline().split())
m,n = map(int, sys.stdin.readline().split())

apples=[]
oranges=[]

for i in list(map(int, sys.stdin.readline().split())):
    apples.append(i+a)
    
for i in list(map(int, sys.stdin.readline().split())):
    oranges.append(i+b)

count = 0
for i in apples:
    if i >= s and i <= t:
        count = count + 1
print(count)
    
count = 0
for i in oranges:
    if i >= s and i <= t:
        count = count + 1
print(count)
    