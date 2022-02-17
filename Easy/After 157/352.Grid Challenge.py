import sys

def gridchallenge(n,grid):
    for i in range(len(grid[0])):
        for j in range(n-1):
            if grid[j][i] > grid[j+1][i]:
                #print(chr(grid[j][i]),chr(grid[j+1][i]))
                return "NO"
    return "YES"
for i in range(int(input())):
    n = int(input())
    grid = []
    temp = []
    for j in range(n):
        temp = list("".join(sys.stdin.readline().rstrip()))
        for j in range(len(temp)):
            temp[j] = ord(temp[j])
        grid.append(sorted(temp))
    
    print(gridchallenge(n,grid))