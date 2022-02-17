import sys

n, k = map(int, sys.stdin.readline().split())
prices = list(map(int, sys.stdin.readline().split()))
prices = [ x for  x in sorted(prices) if x <= k]
answer : int = 0
current : int = 0
for i in prices:
    if current+i <= k :
        current += i
        answer +=1
    else:
        break

print(answer)
