import sys

n=int(input().rstrip())
password=sys.stdin.readline().rstrip()
array = list("".join(password))
condition = [0, 0, 0, 0]
special =[33, 64, 35, 36, 37, 94, 38, 42, 40, 41, 45, 43] 
#check digit
#check lowercase
#check uppercase
#check special

for i in array:
    if condition.count(1)==4:
        break
    if not condition[0]:
        if i.isdecimal():
            condition[0] = 1
            continue
    if not condition[1]:
        if ord(i)>=97 and ord(i)<=122:
            condition[1] = 1
            continue
    if not condition[2]:
        if ord(i)>=65 and ord(i)<=90:
            condition[2] = 1
            continue
    if not condition[3]:
        if ord(i) in special:
            condition[3] = 1
            continue

#A to Z 65 90
#a to z 97 122
if len(array)>=6:
    print(condition.count(0))
else:
    print(max(condition.count(0),6-len(array)))