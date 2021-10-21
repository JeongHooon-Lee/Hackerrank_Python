#https://www.hackerrank.com/challenges/utopian-tree/problem?isFullScreen=true

import sys



for i in range(int(input())):
    answer = 1
    n = int(sys.stdin.readline())
    for j in range(n):
        if j % 2 == 0:
            answer = answer * 2
        elif j % 2 == 1:
            answer += 1
    print(answer)