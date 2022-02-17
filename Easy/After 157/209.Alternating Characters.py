import sys

for i in range(int(input().rstrip())):
    count = 0
    s = sys.stdin.readline().rstrip()
    for a, b in zip(s[:-1], s[1:]):
        if a == b:
            count+=1
    print(count)