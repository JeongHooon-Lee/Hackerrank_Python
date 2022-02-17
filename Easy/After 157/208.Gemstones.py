import sys

arr = []
alpha = []
alpha2 = []
for i in range(int(input().rstrip())):
    arr.append(sys.stdin.readline().rstrip())

for i in arr[0]:
    if i in alpha:
        continue
    else:
        alpha.append(i)

# print(alpha)
for i in arr[1:]:
    for j in alpha:
        if j not in i:
            alpha2.append(j)
    alpha = [ x for x in alpha if x not in alpha2 ]
    #print(alpha)
print(len(alpha))