import sys

for i in range(int(input().rstrip())):
    array = [ 0 for _ in range(26) ]
    answer = 0
    s1 = sys.stdin.readline().rstrip()
    s2 = sys.stdin.readline().rstrip()

    for i in s1:
        array[ord(i)-97] +=1
    
    for i in s2:
        if array[ord(i)-97] > 0:
                answer=1
                break
    if answer == 1:
        print("YES")
    else:
        print("NO")
    
