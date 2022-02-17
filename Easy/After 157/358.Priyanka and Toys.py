import sys

n = int(input().strip())
arr = list(map(int, sys.stdin.readline().split()))
arr = sorted(arr)
answer = 1
temp = arr[0]
for i in range(1,n):
    if arr[i] in range(temp,temp+5):
        continue
    elif arr[i] not in range(temp, temp+5):
        temp = arr[i]
        answer +=1  
print(answer)