#https://www.hackerrank.com/challenges/dynamic-array/problem?h_r=next-challenge&h_v=zen
import sys

def dynamicArray(n, queries):
    # Write your code here
    arr=[ [] for _ in range(n) ]
    lastAnswer=0
    answer=[]
    for i in queries:
        idx=( i[1] ^ lastAnswer) % n
        if i[0] == 1:
            arr[idx].append(i[2])
            #print(arr)
        elif i[0] == 2:
            lastAnswer = arr[idx][ ( i[2] % len(arr[idx]) ) ]
            print(lastAnswer)

            
    #print(arr)    
first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])
q = int(first_multiple_input[1])


queries = []

for _ in range(q):
    queries.append(list(map(int, input().rstrip().split())))

result = dynamicArray(n, queries)

