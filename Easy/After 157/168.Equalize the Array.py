import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

temp2 = []
temp = list(set(arr))

for i in range(len(temp)):
    temp2.append(arr.count(temp[i]))


print(n-max(temp2))