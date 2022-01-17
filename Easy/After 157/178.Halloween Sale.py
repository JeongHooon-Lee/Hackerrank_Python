import sys

p, d, m, s = map(int, sys.stdin.readline().split())

price = p
result = 0
while True:
    if s-price < 0:
        break
    s = s - price
    
    if price-d < m:
        price = m
    else:
        price = price - d
    
    result=result+1
print(result)