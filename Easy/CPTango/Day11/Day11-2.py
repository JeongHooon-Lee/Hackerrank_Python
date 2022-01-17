#https://www.hackerrank.com/challenges/birthday-cake-candles/problem
import sys

N = int(sys.stdin.readline())
candles = list(map(int, sys.stdin.readline().split()))

print(candles.count(max(candles)))