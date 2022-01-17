import sys

t = int(input().rstrip())
time = 1
x=3
value =0

while True:
    if x <= (t+2) and (t+2) < x*2:
        value = 2*x-t-2
    if value !=0:
        break
    x = x*2
print(value)