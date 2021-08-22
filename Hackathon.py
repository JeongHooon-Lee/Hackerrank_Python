import sys

def sumarray(s):
    a=""
    for i in range(len(s)):
        a= a+ s[i]
    return a

def solution(s):
    
    if len(s) == 0:
        return ""
    elif len(s) == 1:
        return s
    
    answer = [s[0]] #중복을 모두 제거
    ban=s[0]
    tmp=-1
    a=""
    result=[]
    
    
    for i in range(1,len(s)):
        if s[i] is not ban:
                answer.append(s[i])
                ban=s[i]
        elif s[i] is ban:
            tmp=i-1
            answer.remove(s[i])
            for j in range(i+1,len(s)):
                if s[j] is ban:
                    continue
                else:
                    for k in range(j,len(s)):
                        answer.append(s[k])
                    break
            break
    print(answer,tmp)
    
    for i in range(tmp):
        a = a + s[i]
    result.append(a)
    print(result)
    print(answer[tmp:])
    if not answer[tmp:]:
        result=result
    else:
        result=result+solution(answer[tmp:])
    return result

s = list(sys.stdin.readline().rstrip())
print(solution(s))
