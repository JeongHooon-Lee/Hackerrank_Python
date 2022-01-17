import sys

s = sys.stdin.readline().rstrip()
t = sys.stdin.readline().rstrip()
k = int(sys.stdin.readline())


if len(s) >= len(t):
    for i in range(min(len(s),len(t))):
        if s[i] != t[i]:
            break
        else:
            continue

    if (len(s)-i)+(len(t)-i) <= k:
        print("Yes")
    # elif len(s)+len(t) <= k:
    #     print("yes")
    else:
        print("No")

else:
    for i in range(min(len(s),len(t))):
        if s[i] != t[i]:
            break
        elif i == min(len(s),len(t))-1:
            i = len(t)-len(s)
            break
        else:
            continue

    if len(s)>=len(t):
        if (len(s)-i)+(len(t)-i) <= k:
            print("Yes")
        # elif len(s)+len(t) <= k:
        #     print("yes")
        else:
            print("No")
    else:
        if (k-(len(t)-len(s)))%2 == 0:
            print("Yes")
        else:
            print("No")
