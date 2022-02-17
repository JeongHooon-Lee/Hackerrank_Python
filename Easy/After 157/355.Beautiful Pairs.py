import sys

n = int(input().rstrip())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))
array = [0 for _ in range(1001)] 
answer = 0
if n==1:
    print(0)
    quit()
for i in a:
    array[i] +=1
for i in b:
    if array[i] >0:
        answer +=1
    array[i] -=1
if list(filter(lambda x: x>0, array)) and list(filter(lambda x: x<0, array)):
    print(answer+1)
elif not list(filter(lambda x: x!=0, array)):
    print(answer-1)
else:
    print(answer)
