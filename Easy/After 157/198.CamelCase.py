import sys

print(ord("A"),ord("Z"))
s = sys.stdin.readline().rstrip()
s = list("".join(s))
count=1
for i in s:
    if ord(i)>=65 and ord(i) <= 90:
        count = count + 1
print(count)