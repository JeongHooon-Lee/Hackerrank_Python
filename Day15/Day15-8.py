#https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem?isFullScreen=true

import sys

i,j,k = map(int, sys.stdin.readline().split())

def factory(num):
    tmp = list(str(num))
#    print(tmp)
    tmp = reversed(tmp)
#    print(tmp)    
    tmp = "".join(tmp)
    return(int(tmp))

count =0
for q in range(i,j+1):
    if abs(q-factory(q))%k == 0:
        count+=1

print(count)