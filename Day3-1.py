import sys
A= int(input().strip())
N= list(map(int, sys.stdin.readline().rstrip().split()))

#rint(' '.join(map(str,reversed(N))))
temp=[]
for i in reversed(N):
    temp.append(i)

print(' '.join(map(str,temp)))