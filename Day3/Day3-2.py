import sys

N=sys.stdin.readline().strip()

answer=0
for i in range(len(N)):
    try:
        answer += (16 ** (len(N)-i-1)) * int(N[i])
    except:
        answer += (16 ** (len(N)-i-1)) * (ord(N[i])-55)
    
print(answer)