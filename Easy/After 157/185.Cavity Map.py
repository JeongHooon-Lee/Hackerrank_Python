import sys

grid = []
n=int(sys.stdin.readline())
for i in range(n):
    temp = int(sys.stdin.readline().rstrip())
    temp = list(map(int, str(temp)))
    grid.append(temp)

#print(grid)
result = []
for i in range(1,n-1):
    for j in range(1,n-1):
        if grid[i][j] > grid[i-1][j] and grid[i][j] > grid[i+1][j] and grid[i][j] > grid[i][j-1] and grid[i][j] > grid[i][j+1]:
            result.append((i,j))

for a, b in result:
    grid[a][b] = "X"

for i in range(n):
    temp = map(str, grid[i])
    print("".join(temp))
