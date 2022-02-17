from operator import rshift
import sys


for i in range(int(input().rstrip())):
    answer=0
    arr = []
    s = sys.stdin.readline().rstrip()
    for i in s:
        arr.append(ord(i))
    rev_arr=list(reversed(arr))
    for a, b, c, d in zip(arr[:-1], arr[1:], rev_arr[:-1], rev_arr[1:]):
        if abs(a-b) != abs(c-d):
            answer=1
            break
    if answer==1:
        print("Not Funny")
    else:
        print("Funny")
    