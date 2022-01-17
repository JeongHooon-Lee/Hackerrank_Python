import sys

n = int(sys.stdin.readline())
c = list(map(int, sys.stdin.readline().split()))

current=0
count=0

while True:
    if current+1 == n-1:
        count = count + 1
        break
    elif current+2 == n-1:
        count = count + 1
        break
    else:
        if c[current+2] == 0:
            current = current+2
        else:
            current = current+1
        count = count +1
print(count)


    