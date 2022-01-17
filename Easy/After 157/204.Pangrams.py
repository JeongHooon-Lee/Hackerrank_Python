import sys

s = sys.stdin.readline().rstrip().replace(" ","")
s = s.lower()
temp = []
for i in range(97,123):
    temp.append(chr(i))

else:
    for i in s:
        if i in temp:
            temp.remove(i)

if len(temp) == 0:
    print("pangram")
else:
    print("not pangram")