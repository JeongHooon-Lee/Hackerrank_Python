import sys

p = int(sys.stdin.readline())
q = int(sys.stdin.readline())

result = []
for i in range(p,q+1):
    square = i * i
    l_num = 0
    temp = list(str(square))
    #print(temp[:len(temp)//2])
    #print(temp[len(temp)//2:])
    if square > 10:
        l_num = int(''.join(temp[:len(temp)//2]))
    r_num = int(''.join(temp[len(temp)//2:]))

    if l_num+r_num == i:
        result.append(i)

if len(result)==0:
    print("INVALID RANGE")
else:
    for i in result:
        print(i,end=" ")