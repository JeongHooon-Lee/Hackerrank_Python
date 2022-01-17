import sys

for i in range(int(input().rstrip())):
    n = int(input().rstrip())
    b = list(input().rstrip())

    temp = sorted(list(set(b)))
  #  print(temp)
    even = 0
    for i in temp:
        if i == "_":
            break
        if b.count(i) == 1:
            even = 1
            break
    if even == 1:
        print("NO")            
    elif b.count("_") and even == 0:
        print("YES")
    else:
        temp2=0
        for j in range(n-1):
            if b[j] != b[j+1] and temp2 == 0:
                print("NO")
                break
            elif b[j] == b[j+1]:
                temp2=1
            elif b[j] != b[j+1]:
                temp2=0
        if temp2 == 1:
            print("YES")