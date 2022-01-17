import sys

n = int(input().rstrip())
array = list("".join(sys.stdin.readline().rstrip()))
k = int(input().rstrip())
answer =[]
k %= 26

for i in range(len(array)):
    if ord(array[i]) >= 97 and ord(array[i]) <= 122:
        if ord(array[i])+k > 122:
            sys.stdout.write(chr(ord(array[i])+k-26))
            #@print(chr(ord(array[i])+k-26))
            #print(ord(array[i])+k-26)
        else:
            sys.stdout.write(chr(ord(array[i])+k))
    elif ord(array[i]) >= 65 and ord(array[i]) <= 90:
        if ord(array[i])+k > 90:
            sys.stdout.write(chr(ord(array[i])+k-26))
        else:
            #print(chr(ord(array[i])+2))
            sys.stdout.write(chr(ord(array[i])+k))
    else:
        sys.stdout.write(array[i])