from locale import ABMON_10
import sys

n = int(input())
array : list =[]

for i in range(n):
    a, b= map(int, sys.stdin.readline().split())
    array.append((i+1,a+b))

array=sorted(array, key =lambda x : x[1])


for i in range(len(array)):
    print(array[i][0], end = " ")
