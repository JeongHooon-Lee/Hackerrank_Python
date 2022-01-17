import sys

for i in range(int(sys.stdin.readline())):
    b, w = map(int, sys.stdin.readline().split())
    bc, wc, z = map(int, sys.stdin.readline().split())

    if bc >= wc+z:
        bc = wc+z
    if wc >= bc+z:
        wc = bc+z
    
    print(b*bc+w*wc)