import sys
import math

for i in range(int(sys.stdin.readline())):
    a, b = map(int, sys.stdin.readline().split())
    temp1 = math.sqrt(a)
    temp2 = math.sqrt(b)

    temp1 = math.ceil((temp1))
    temp2 = int(temp2)
    print(temp2-temp1+1)