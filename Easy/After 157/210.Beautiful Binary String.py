import sys

n = int(input().rstrip())
b = sys.stdin.readline().rstrip()
count = 0

if n < 3:
    print(count)
else:
    i=0
    while True:
        if i > n-3:
            break
        else:
            if b[i] == "0" and b[i+1] == "1" and b[i+2] == "0":
                count+=1
                i += 3 
            else:
                i+=1

    print(count)