from operator import rshift
import sys


import sys


def check(s):
    rev_S = "".join(list(reversed(s)))
    # print(rev_S,"".join(s))
    if rev_S == "".join(s):
        return 1
    else:
        return -1

for i in range(int(input().rstrip())):
    s = list(sys.stdin.readline().rstrip())
    # print(s)
    if check(s)==1:
        print(-1)
    else:
        for i in range(len(s)//2):
            if s[i] != s[-(i+1)]:
                del s[i]
                if check(s)==1:
                    print(i)
                    break
                else:
                    print(len(s)-i)
                    break
        continue

