from itertools import combinations
import sys

def func(arr):
    answer = []
    for i in arr:
        if sum(i) - max(i) > max(i):
            if len(answer) == 0:
                answer += i
            elif sum(answer) < sum(i):
                answer = i
    if len(answer) == 0:
        return "-1"
    else: 
        return " ".join(map(str, sorted(answer)))

n = int(input())
array = list(map(int, sys.stdin.readline().split()))
arr = combinations(array,3)

print(func(arr))
