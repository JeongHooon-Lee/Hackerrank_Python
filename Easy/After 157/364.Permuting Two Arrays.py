import sys

q = int(input())
for i in range(q):
    answer=0
    n, k = map(int, sys.stdin.readline().split())
    A_array = list(map(int, sys.stdin.readline().split()))
    B_array = list(map(int, sys.stdin.readline().split()))
    A_array.sort()
    B_array.sort(reverse=1)
    
    for a, b in zip(A_array, B_array):
        if a+b<k:
            answer = 1
            break
    if answer == 0:
        print("YES")
    elif answer == 1:
        print("NO")

    

    