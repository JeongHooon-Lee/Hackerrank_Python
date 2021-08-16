#https://www.hackerrank.com/challenges/2d-array/problem
import sys

def hourglassSum(arr):
    A=-72
    for i in range(4):
        for j in range(4):
            temp=[]
            temp.append(arr[i][j])
            temp.append(arr[i][j+1])
            temp.append(arr[i][j+2])
            temp.append(arr[i+1][j+1])
            temp.append(arr[i+2][j])
            temp.append(arr[i+2][j+1])
            temp.append(arr[i+2][j+2])
            
            if A < sum(temp):
                A=sum(temp)
                
            temp=[]
                
    return(A)
            
arr=[]
for _ in range(6):
    arr.append(list(map(int, input().rstrip().split())))
    
result = hourglassSum(arr)
print(result)