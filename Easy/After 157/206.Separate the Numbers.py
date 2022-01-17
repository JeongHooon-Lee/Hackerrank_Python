import sys

def validate(s, first):
    while s:
        if s.startswith(first):
            s = s[len(first):]
            first = str(int(first)+1)
        else:
            return False
    return True

for i in range(int(input().strip())):
    s = sys.stdin.readline().rstrip()

    if s[0] == '0' and len(s) > 1:
        print("NO")
    else:
        for i in range(1, len(s)//2 + 1):
            first = s[:i]
            if validate(str(s), first):
                print("YES " + first)
    print("NO")