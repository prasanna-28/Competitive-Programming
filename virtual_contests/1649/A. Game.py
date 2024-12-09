import sys
import math
import operator
from collections import deque, defaultdict, Counter, OrderedDict
from functools import cache, partial, reduce
from itertools import *

MOD       = 10**9 + 7
INF       = float('inf')
NINF      = float('-inf')
YES,NO    = "YES", "NO"
DEBUG     = 0
CONTRACTS = 1
MT        = 1
OUT       = []

#---------------------------------------------------
def sol():
    n = ipt()
    a = ilist()
    i = n - 1
    while i > 0 and a[i-1]:
        i -= 1
    for k in range(n-1):
        if not a[k+1]:
            break

    print(i - k if i-k > 0 else 0)



#---------------------------------------------------
def main():
    if MT:
        for _ in range(ipt()):
            sol()
    else:
        sol()

if __name__ == "__main__":
    finp        = sys.stdin.readline
    njoin       = lambda x: '\n'.join(map(str, x))
    ljoin       = lambda x: ' '.join(map(str, x))
    sjoin       = lambda x: '\n'.join(x)
    ilist       = lambda: list(map(int, finp().split()))
    slist       = lambda: list(input())
    slists      = lambda: input().split()
    ivars       = lambda: map(int, finp().split())
    ipt         = lambda: int(finp())
    debug       = lambda **kwargs: (print("Dbg:"), print("\n".join([f"{key} = {value}" for key, value in kwargs.items()]))) if DEBUG else None

    main()

