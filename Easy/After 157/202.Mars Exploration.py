import sys

array = list("".join(sys.stdin.readline().rstrip()))
answer = 0
for i in range(len(array)):
    if i % 3 == 1:
        if array[i] != "O":
            answer +=1
    else:
        if array[i] != "S":
            answer +=1
print(answer)