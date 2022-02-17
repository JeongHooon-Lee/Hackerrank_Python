import sys

n = int(input().strip())
answer =0
if n == 0:
    print(1)
    quit()
n = bin(n)[2:]
print(pow(2,n.count('0')))