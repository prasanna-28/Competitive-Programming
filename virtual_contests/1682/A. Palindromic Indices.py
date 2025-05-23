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
ivars  = lambda: map(int, finp().split())
ipt    = lambda: int(finp())
debug  = lambda **kwargs: (print("Dbg:"), print("\n".join([f"{key} = {value}" for key, value in kwargs.items()]))) if DEBUG else None

#---------------------------------------------------
def sol():
    n = ipt()
    s = slist()
    k = s[(n-1)//2]
    if n%2 == 1:
        l = (n-1)//2 - 1
        res = 1
        while l >= 0 and s[l] == k:
            l -= 1
            res += 2
        print(res)
    else:
        res = 2
        l = (n-2)//2 - 1
        while l >= 0 and s[l] == k:
            l -= 1
            res += 2
        print(res)


#---------------------------------------------------
if __name__ == "__main__":
    for _ in range(ipt()): sol()
    #sol()
    pass
