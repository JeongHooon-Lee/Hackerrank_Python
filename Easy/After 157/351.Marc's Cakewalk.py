import sys

n = int(input())
c = list(map(int, sys.stdin.readline().split()))
answer =0
c = sorted(c,reverse=1)
for i in range(n):
    answer += pow(2,i)*c[i]
print(answer)