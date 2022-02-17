import sys

n = int(input().rstrip())
arr = list(map(int, sys.stdin.readline().split()))
answer : list = []

arr = sorted(arr)

temp = abs(arr[0]-arr[1])
for a, b in zip(arr[1:-1],arr[2:]):
    if abs(a-b) < temp:
        answer = []
        temp = abs(a-b)
        answer.append(a)
        answer.append(b)
    elif abs(a-b) == temp:
        answer.append(a)
        answer.append(b)

for  i in answer:
    print(i, end=" ")