import sys

for i in range(int(input().rstrip())):
    answer = 0
    q = sys.stdin.readline().rstrip()

    string_len=len(q)//2

    for i in range(string_len):
        answer += abs(ord(q[i]) - ord(q[-(i+1)]))
    print(answer)