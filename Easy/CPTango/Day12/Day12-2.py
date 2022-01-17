#https://www.hackerrank.com/challenges/kangaroo/problem

import sys

x1,v1,x2,v2 = map(int, sys.stdin.readline().split())


if x1 < x2 and v1 < v2:
    print("NO")
elif x1 > x2 and v1 > v2:
    print("NO")
elif x1 < x2 and v1 > v2:
    if (x2-x1)%(v1-v2)==0:
        print("YES")
    else:
        print("NO")
elif x1 > x2 and v1 < v2:
    if (x1-x2)%(v2-v1)==0:
        print("YES")
    else:
        print("NO")
        
elif v1 == v2 and x1 == x2:
    print("YES")
else:
    print("NO")