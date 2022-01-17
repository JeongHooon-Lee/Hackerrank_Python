import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

result = 1001
for i in range(len(arr)):
    if arr[i+1:].count(arr[i]) == 0:
        continue

    if 1+arr[i+1:].index(arr[i])<result:
        result = arr[i+1:].index(arr[i])+1
if result == 1001: 
    reuslt = -1
print(result)