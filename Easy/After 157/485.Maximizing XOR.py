import sys

l = int(input().strip())
r = int(input().strip())
answer = 0
for i in range(l,r+1):
    for j in range(i,r+1):
        if i ^ j > answer:
            answer = i^j
print(answer)