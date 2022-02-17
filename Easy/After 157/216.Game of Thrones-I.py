from itertools import count
import sys

s = sys.stdin.readline().rstrip()
alpha = [0 for _ in range(26)]

for i in s:
    alpha[ord(i)-97] += 1

count_odd : int = 0
for i in alpha:
    if i%2 == 1:
        count_odd +=1

if len(s)%2 == 1:
    if count_odd == 1:
        print("YES")
    else:
        print("NO")
else:
    if count_odd > 0:
        print("NO")
    else:
        print("YES")