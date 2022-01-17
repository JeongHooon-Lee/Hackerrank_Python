import sys

n, k = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

result = 0
page = 1
storage = []

for i in arr:
    for j in range(1,i+1):
        if len(storage) == k:
            storage = []
            page = page + 1
        storage.append(j)
        if j == page:
            result = result + 1
    page = page + 1
    storage = []

print(result)