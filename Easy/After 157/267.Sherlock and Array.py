import sys

def fun(n,arr):
    left_sum = 0
    right_sum = sum(arr)
    for i in range(n):
        right_sum -= arr[i]
        if right_sum == left_sum:
            return "YES"
        left_sum +=arr[i]
    return "NO"

for i in range(int(input())):
    n = int(input())
    arr = list(map(int, sys.stdin.readline().split()))
    answer = 0
    if n==1:
        print("YES")
        continue
    print(fun(n,arr))
