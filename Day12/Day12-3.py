#https://www.hackerrank.com/challenges/between-two-sets/problem
import sys
from math import gcd

n, m = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

# Greatest Common Divisor
# 최대공약수 gcd(a,b)

# Least common multiple
# 최소공배수
def lcm (a,b):
    return int( a*b / gcd(a,b) )

# 리스트의 최소공배수
def list_lcm(array):
    result=None
    for i in range(len(array)):
        if i == 0:
            result = array[i]
        else:
            result = lcm(result,array[i])
    return result

# 리스트의 최대공약수
def list_gcd(array):
    result=None
    for i in range(len(array)):
        if i == 0:
            result = array[i]
        else:
            result = gcd(result,array[i])
    return result

LcmA=list_lcm(a)
GcdB=list_gcd(b)


tmp=1
answer=[]
while True:
    if tmp*LcmA > GcdB:
        break
    if GcdB % (tmp*LcmA) == 0:
        answer.append(tmp*LcmA)
    tmp+=1

print(len(answer))
