import sys

for i in range(int(input().rstrip())):
    alpha = [ 0 for _ in range(26) ]
    answer = 0
    s = sys.stdin.readline().rstrip()
    for i in s:
        if alpha[ord(i)-97] == 0:
            answer +=1 
            alpha[ord(i)-97] +=1
    print(answer)