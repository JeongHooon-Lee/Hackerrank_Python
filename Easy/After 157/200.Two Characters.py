import sys
from itertools import combinations

n=int(input().rstrip())
s=sys.stdin.readline().rstrip()
array=list("".join(s))
temp=set(array)
temp2 = []
answer = []



for a,b in combinations(temp,2):
    temp2.append([a,b])
    temp3 = [x for x in array if x==a or x==b]
    for i in range(len(temp3)-1):
        if temp3[i] != temp3[i+1]:
            if i == len(temp3)-2:
                answer.append(len(temp3))
            continue
        else:
            break
        
if len(answer) == 0:
    print(0)
else:
    print(max(answer))