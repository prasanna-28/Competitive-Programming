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
    maxes = []
    for i in range(1, n-1):
        if a[i-1] < a[i] > a[i+1]:
            maxes.append(i)
    tot = len(maxes)
    seen = set()
    i = 0
    while i < len(maxes):
        if maxes[i-1] + 2 == maxes[i]:
            a[maxes[i-1] + 1] = max(a[maxes[i-1]], a[maxes[i]])
            tot -= 1

            seen.add(maxes[i-1])
            seen.add(maxes[i])
            i += 2
            continue
        a[maxes[i] + 1] = a[maxes[i]]
        seen.add(maxes[i])
        i += 1
    for i in maxes:
        if i not in seen:
            a[i + 1] = a[i]
    print(tot)
    print(ljoin(a))

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

