#https://www.hackerrank.com/challenges/designer-pdf-viewer/problem?isFullScreen=true

import sys

heights = list(map(int, sys.stdin.readline().split()))

string = sys.stdin.readline().rstrip()
string = list(string)

Max=-1
for i in string:
    if Max <= heights[ord(i)-97]:
        Max = heights[ord(i)-97]
    
return Max*len(string)
#a=97