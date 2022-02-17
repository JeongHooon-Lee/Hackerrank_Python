import sys

s1 = sys.stdin.readline().rstrip()
s2 = sys.stdin.readline().rstrip()
answer : int = 0
array = [ 0 for _ in range(26)]

for i in s1:
    array[ord(i)-97] += 1

for i in s2:
    if array[ord(i)-97] > 0:
        array[ord(i)-97] -= 1
    else:
        answer +=1
        
for i in array:
    if i == 0:
        continue
    else:
        answer +=i

print(answer)