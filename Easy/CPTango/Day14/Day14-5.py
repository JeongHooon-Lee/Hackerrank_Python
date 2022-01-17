#https://www.hackerrank.com/challenges/counting-valleys/problem?isFullScreen=true

import sys
import collections

steps = int(sys.stdin.readline())
path = sys.stdin.readline().rstrip()
a=list(path)
level=1
answer=0
for i in a:
    if i == 'U':
        level+=1
        if level == 1:
            answer +=1
    else:
        level-=1
    
print(answer)