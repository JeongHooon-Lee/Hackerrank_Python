import math
import os
import random
import re
import sys

def weightedUniformStrings(s, queries):
    weight_chart : dict = {}
    for i in range(26):
        weight_chart[chr(97+i)] = i+1
    answer : set = set()
    result : list = []
    weightsum : int = 0
    prev : str = ''
 
    # for i in range(len(s)):
    #     if s[i] == prev:
    #         answer.append(answer[-1]+weight_chart[s[i]])
    #     else:
    #         prev = s[i]
    #         answer.append(weight_chart[s[i]])
            
    for i in s:
        if i == prev:
            weightsum += weight_chart[i]
            answer.add(weightsum)
        else:
            weightsum = weight_chart[i]
            prev = i
            answer.add(weight_chart[i])

    for i in queries:
        if i in answer:
            result.append("Yes")
        else:
            result.append("No")
    return result

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = sys.stdout

    s = input()

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()