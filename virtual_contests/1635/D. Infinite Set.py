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
MT        = 0
OUT       = []

#---------------------------------------------------
def sol():
    _,p = ivars()
    a = ilist()

    # dp[i][k in {0,1}]
    # number of numbers where bit is k at position i
    # 2n+1 and 4n leads to following transitions:
    # dp[i][0] = dp[i-2][0] + dp[i-2][1]
    # dp[i][1] = dp[i-1][1] + dp[i-1][0]
    # or if we go bottom up:
    # dp[i+2][0] += dp[i][0] + dp[i][1]
    # dp[i+1][1] += dp[i][0] + dp[i][1]

    t = set(a)
    for i in a:
        curr = i
        while i > 0:
            if i & 1:
                i>>=1
            elif not (i>>1) & 1:
                i >>= 2
            else:
                break
            if i in t:
                t.remove(curr)
                break

    a = t

    dp = [[0,0] for _ in range(p+1)]
    for i in a:
        if i & 1 and len(bin(i)) - 2 < len(dp):
            dp[len(bin(i)) - 2][1] += 1
        elif len(bin(i)) - 2 < len(dp):
            dp[len(bin(i)) - 2][0] += 1

    for i in range(p+1):
        if i+2 < len(dp):
            dp[i+2][0] += dp[i][0]
            dp[i+2][0] += dp[i][1]
            dp[i+2][0] %= MOD
        if i+1 < len(dp):
            dp[i+1][1] += dp[i][0]
            dp[i+1][1] += dp[i][1]
            dp[i+1][1] %= MOD
    s = 0
    for i in range(p+1):
        s += sum(dp[i])
        s %= MOD

    print(s)
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

