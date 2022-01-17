#https://www.hackerrank.com/challenges/grading/problem
import sys

array=[]
for i in range(int(input())):
    tmp = int(sys.stdin.readline())
    if tmp < 38:
        array.append(tmp)
    else:
        if (tmp+1) % 5 == 0:
            array.append(tmp+1)
        elif (tmp+2) % 5 == 0:
            array.append(tmp+2)
        else:
            array.append(tmp)

for i in array:
    print(i)