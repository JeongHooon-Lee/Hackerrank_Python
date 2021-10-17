#https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem
#https://www.youtube.com/watch?v=bKW4O3IclYU

import sys

n = int(sys.stdin.readline())

scores=list(map(int, sys.stdin.readline().split()))
Count=[0,0]

Min = -1
Max = -1
for i in range(len(scores)):
    if i==0:
        Min=scores[i]
        Max=scores[i]
    else:
        if scores[i] > Max:
            Max = scores[i]
            Count[0]+=1
        elif scores[i] < Min:
            Min = scores[i]
            Count[1]+=1

print(Count[0],Count[1])
    