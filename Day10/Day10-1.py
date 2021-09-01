#https://www.hackerrank.com/challenges/qheap1/problem
# import sys
# import heapq


# Q=int(sys.stdin.readline().rstrip())

# heap=[]

# for i in range(Q):
#     ipt = list(map(int, sys.stdin.readline().split()))
#     if ipt[0] == 1:
#         heapq.heappush(heap, ipt[1])
#     elif ipt[0] == 2:
#         heap.remove(ipt[1])
#     else:
#         print(min(heap))
    
#     print(heap)
from sys import stdin
from heapq import heappush, heappop

heap = []
item_lookup = set()

def push(v):
    heappush(heap, v)
    item_lookup.add(v)
    
def discard(v):
    item_lookup.discard(v)
    
def print_min():
    while heap[0] not in item_lookup:
        heappop(heap)
    print(heap[0])
    
cmds = {
    1: push,
    2: discard,
    3: print_min
}

n = int(stdin.readline())
for _ in range(n):
    data = map(int,stdin.readline().split(" "))
    cmds[data[0]](*data[1:])