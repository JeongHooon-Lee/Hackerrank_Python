import sys

s = sys.stdin.readline().split()
s = list(" ".join(s))
print(s)

while True:
    temp = len(s)
    for i in range(len(s)-1):
        if s[i]==s[i+1]:
            del s[i]
            del s[i]
            break
    if len(s)==0 or len(s) == 1:
        break
    if len(s) == temp:
        break
if len(s) == 0:
    print("Empty String")
else:
    print("".join(s))
