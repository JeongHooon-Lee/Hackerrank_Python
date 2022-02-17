import sys
n = int(input())

arr = list(map(int, sys.stdin.readline().split()))
equal = arr[0]
right : list = []
left : list = []

for i in arr[1:]:
    if i > equal:
        right.append(i)
    elif i < equal:
        left.append(i)
print(" ".join(map(str, left)) + " " + str(equal) + " " + " ".join(map(str, right)))