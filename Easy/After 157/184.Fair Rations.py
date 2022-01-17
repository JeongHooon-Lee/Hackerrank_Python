import sys

n = int(sys.stdin.readline())
b = list(map(int, sys.stdin.readline().split()))

print(b)

temp = -1
result = 0

for i in range(n-1):
    if b[i]%2 != 0 and temp != -1:
        b[i] = b[i] + 1
        result = result + (i-temp)*2
        temp = -1
    elif b[i]%2 == 1 and b[i+1]%2 == 1:
        b[i] = b[i] + 1
        b[i+1] = b[i+1] + 1
        result = result + 2
        temp = -1
    elif b[i]%2 == 1 and b[i+1]%2 != 1:
        b[i] = b[i] + 1
        temp = i

if temp != -1 and b[-1]%2 == 1:
    result = result + (n-temp-1)*2
if temp != -1 and b[-1]%2 == 0:
    print("NO")
elif temp == -1 and b[-1]%2 == 1:
    print("NO")
else:
    print(result)



