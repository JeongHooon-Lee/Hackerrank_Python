import sys

for i in range(int(input().strip())):
    n = int(input().strip())
    if n % 7 < 2:
        print("Second")
    else:
        print("First")