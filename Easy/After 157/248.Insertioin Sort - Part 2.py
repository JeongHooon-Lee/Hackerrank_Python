import sys

n = int(input())
arr = list(map(int ,sys.stdin.readline().split()))

for i in range(n-1):
    for j in range(i,-1,-1):
        if arr[j]>arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
    for k in arr:
        print(k,end=' ')
    print("")