import sys

n, d = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

count = 0
storage = []
for i in range(len(arr)):
    if arr[i] in storage:
        continue
    if arr[i] + 2*d > arr[-1]:
        continue
    
    if arr.count(arr[i]+d) and arr.count(arr[i]+2*d):
        count = count + arr.count(arr[i])*arr.count(arr[i]+d)*arr.count(arr[i]+2*d)
        storage.append(arr[i])

print(count)
