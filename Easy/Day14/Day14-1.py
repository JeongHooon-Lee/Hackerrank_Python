#https://www.hackerrank.com/challenges/day-of-the-programmer/problem

import sys

Days = [ 0,31,28,31,30,31,30,31,31,30,31,30,31 ]
years = int(sys.stdin.readline())

#Julian calendar
if years <= 1917:
    if years % 4 == 0:
        Days[2] = 29
elif years == 1918: transition Julian to Gregorian calendar
    Days[2] = 15
else: # years >=1919 Gregorian calendar
    if (years % 4 == 0 and years % 100 != 0) or years % 400 == 0:
        Days[2] = 29

tmp=0
for i in range(1, len(Days)):
    date = 256 - tmp
    if date < Days[i]:
        month = str(i)
        break
    else:
        tmp+=Days[i]

if int(month) < 10:
    month = '0'+month
print(str(date)+'.'+month+'.'+str(years))