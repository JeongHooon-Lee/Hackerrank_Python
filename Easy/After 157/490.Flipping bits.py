import sys

temp = 0
for i in range(32):
    temp+=pow(2,i)

for i in range(int(input().strip())):
    n=int(input())
    print(temp-n)