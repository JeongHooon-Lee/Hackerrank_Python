#https://www.hackerrank.com/challenges/time-conversion/problem
import sys

def timeConversion(s):
    answer = list(s[0:8])
    if s[8] == 'A':
        if s[0:2] == '12':
            answer[0] = '0'
            answer[1] = '0'
    else:
        if s[0:2] != '12':
            temp = int(s[0:2])+12
            answer[0] = str(temp)[0]
            answer[1] = str(temp)[1]
    return "".join(answer)


s= input()
result = timeConversion(s)

print(result)

#print(s[0:2] == '12')
