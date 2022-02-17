from re import S
import sys


for i in range(int(input())):
    alpha = [ 0 for _ in range(26)]
    answer=0
    s = sys.stdin.readline().rstrip()
    if len(s)%2 == 1: 
        print(-1)
        continue
    else:
        s_opposite = s[len(s)//2:]
        s = s[:len(s)//2]
        for i in s_opposite:
            alpha[ord(i)-97] += 1
        print(alpha)
        for i in s:
            if alpha[ord(i)-97] > 0:
                alpha[ord(i)-97] -= 1
            else:
                answer +=1
        print(alpha)
        print(answer)