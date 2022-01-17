import sys


for i in range(int(input())):
    temp = ["h","a","c","k","e","r","r","a","n","k"]
    array = list("".join(sys.stdin.readline().rstrip()))
    for i in array:
        if len(temp) == 0:
            break
        if i == temp[0]:
            del temp[0] 
    if len(temp) == 0:
        print("YES")
    else:
        print("NO")