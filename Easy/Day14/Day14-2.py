#https://www.hackerrank.com/challenges/bon-appetit/problem?h_r=internal-search
import sys
n, k = map(int, sys.stdin.readline().split())
bill = list(map(int, sys.stdin.readline().split()))
b = int(sys.stdin.readline())

Sum=0
for i in range(len(bill)):
    if i == k:
        continue
    Sum += bill[i]

if b-(Sum//2) > 0:
    print(b-(Sum//2))
else:
    print("Bon Appetit")