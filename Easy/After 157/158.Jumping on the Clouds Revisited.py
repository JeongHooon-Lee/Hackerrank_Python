import sys

n, k = map(int, sys.stdin.readline().split())
c = list(map(int, sys.stdin.readline().split()))
e = 100

i=0
while True:
    inx = (i+k)%n
    if c[inx] == 1:
        e = e-3
    else:
        e = e-1
    i = inx
    if inx == 0:
        break
print(e)
        