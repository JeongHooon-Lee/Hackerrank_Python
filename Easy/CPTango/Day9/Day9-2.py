#https://www.hackerrank.com/challenges/equal-stacks/problem
import sys

h = list(map(int, sys.stdin.readline().split()))

stack = []
for i in range(len(h)):
    stack.append( list(map(int, sys.stdin.readline().split())) )
    stack[i].reverse()
tmp=[]
for i in range(len(stack)):
        tmp.append(sum(stack[i]))
# A=tmp.index(max(tmp))
# tmp[A]= tmp[A] - stack[tmp.index(max(tmp))].pop()

while True:
    if len(list(set(tmp)))==1:
        print(tmp[0])
        break
    else:
        N=tmp.index(max(tmp))
        tmp[N]=tmp[N] - stack[N].pop()
    