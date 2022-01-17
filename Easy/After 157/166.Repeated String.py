import sys

s = list(sys.stdin.readline().rstrip())
n = int(sys.stdin.readline())
temp = s.count("a")

# print(n//len(s)*temp)

# print(s[:n%len(s)].count("a"))

print((n//len(s)*temp)+(s[:n%len(s)].count("a")))