
import sys

n, k = map(int, sys.stdin.readline().split())
contests = []
for i in range(n):
    contests.append(list(map(int, sys.stdin.readline().split())))
contests = sorted(contests, key = lambda x : (-x[1],-x[0]))
answer = 0

for i in range(k):
    answer +=contests[i][0]
for i in contests[k:]:
    if i[1] == 1:
        answer-=i[0]
    else:
        answer+=i[0]

print(answer)
    