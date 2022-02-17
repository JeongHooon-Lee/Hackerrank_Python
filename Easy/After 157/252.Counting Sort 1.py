import sys

n = int(input().rstrip())
arr = list(map(int, sys.stdin.readline().split()))
answer = [ 0 for x in range(100)]

for i in arr:
    answer[i] += 1

print(" ".join(map(str, answer)))
