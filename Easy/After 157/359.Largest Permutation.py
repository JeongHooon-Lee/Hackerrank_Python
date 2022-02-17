import sys

n, k = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
answer = []
maxnum = max(arr)
positions = {}
for i in range(len(arr)):
    positions[arr[i]] = i

for i in range(len(arr)):
    if k == 0:
        break
    if arr[i] == maxnum:
        maxnum -= 1
    
    if arr[i] < maxnum:
        mind = positions[maxnum]
        positions[maxnum], positions[arr[i]] = positions[arr[i]], positions[maxnum]
        arr[i], arr[mind] = arr[mind], arr[i]
        maxnum -=1
        k -= 1

print(" ".join(map(str, arr)))