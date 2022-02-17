import sys

n = int(input().rstrip())
arr = list(map(int, sys.stdin.readline().split()))
answer = [ 0 for x in range(100)]

for i in arr:
    answer[i] += 1

for i in range(100):
    if answer[i] == 0:
        continue
    else:
        for j in range(answer[i]):
            print(i, end= " ")