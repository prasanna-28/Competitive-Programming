import sys
import math
import operator
from collections import deque, defaultdict, Counter, OrderedDict
from functools import cache, partial, reduce
from itertools import *
MOD    = 10**9 + 7
INF    = float('inf')
NINF   = float('-inf')
YES,NO = "YES", "NO"
DEBUG  = 0
finp   = sys.stdin.readline
njoin  = lambda x: '\n'.join(map(str, x))
ljoin  = lambda x: ' '.join(map(str, x))
sjoin  = lambda x: '\n'.join(x)
ilist  = lambda: list(map(int, finp().split()))
slist  = lambda: list(input())
slists = lambda: input().split()
binput = lambda: list(map(int, input()))
ivars  = lambda: map(int, finp().split())
ipt    = lambda: int(finp())
debug  = lambda **kwargs: (print("Dbg:"), print("\n".join([f"{key} = {value}" for key, value in kwargs.items()]))) if DEBUG else None

#---------------------------------------------------
def sol():
    n = ipt()
    d = binput()
    l = d[:]
    o = 0
    for i in d:
        if i:
            o += 1
    if o == 0 or o%2:
        print("NO")
        return
    else:
        print("YES")
    d = deque(enumerate(d))
    while not d[-1][1]:
        d.rotate(-1)
    segments = []
    d = list(d)
    start = d[0][0]
    prev = (start + 1) % n
    i = prev

    while i%n != start:
        if l[i%n]:
            segments.append((prev, i%n))
            prev = (i + 1) %n
        i += 1
    for i in segments:
        print(start+1, i[0]+1)
        a,b = i
        while a != b:
            print(a + 1, (a + 1) % n + 1)
            a = (a + 1) % n

#---------------------------------------------------
if __name__ == "__main__":
    for _ in range(ipt()): sol()
    #sol()
    pass
