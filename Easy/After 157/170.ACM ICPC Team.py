import sys

n, m = map(int, sys.stdin.readline().split())
arr = []
answer = [0, 0]
for i in range(n):
    temp = sys.stdin.readline().rstrip()
#    temp = list(map(int, temp))
    arr.append(temp)

# print(arr[1])
# print(int(arr[1]))

for i in range(n-1):
    for j in range(i+1,n):
        count = 0
        temp = str(int(arr[i])+int(arr[j]))
        count = temp.count("1")+temp.count("2")

        # for k in range(m):
        #     if arr[i][k] == 1 or arr[j][k]==1:
        #         count = count + 1
        
        if count > answer[0]:
            answer[0] = count
            answer[1] = 1
        elif  count == answer[0]:
            answer[1] = answer[1] + 1
            
print(answer)