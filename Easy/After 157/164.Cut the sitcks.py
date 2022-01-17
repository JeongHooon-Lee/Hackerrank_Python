import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

answer=[]

while True:
    if min(arr)==1001:
        break
    count=0
    length_of_cut = min(arr)

    for i in range(n):
        if arr[i] != 1001:
            arr[i] = arr[i] - length_of_cut
            if arr[i] == 0:
                arr[i] = 1001
            count = count + 1
    answer.append(count)

print(answer)
