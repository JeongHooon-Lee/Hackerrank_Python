import sys

n = int(input().strip())
a = list(map(int, sys.stdin.readline().split()))
array = [ 0 for x in range(101)]

for i in a:
    array[i] +=1

print(array.index(1))