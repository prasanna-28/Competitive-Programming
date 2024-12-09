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

    RIGHT_EDGE = pow(10, 9)
    LEFT_EDGE  = -RIGHT_EDGE

    n,m = ivars()
    dsu = DSU(n + 1)
    never_meet = defaultdict(list)
    will_meet  = defaultdict(list)
    parents = [0] * (n+1)
    for _ in range(m):
        t, u, v = ivars()
        if parents[u] == 0:
            parents[u] = v
        else:
            dsu.union(parents[u], v)
        if parents[v] == 0:
            parents[v] = u
        else:
            dsu.union(u, parents[v])

        if dsu.get(u) == dsu.get(v):
            print(NO)
            return
        if t == 1:
            never_meet[u].append(v)
            never_meet[v].append(u)
        else:
            will_meet[u].append(v)
            will_meet[v].append(u)

    print(YES)
    res = [[] for _ in range(n+1)]






#---------------------------------------------------

class DSU:
    def __init__(self, n):
        self.p = [i for i in range(n)]
        self.r = [1 for _ in range(n)]

    def get(self, a):
        if self.p[a] == a:
            return a
        self.p[a] = self.get(self.p[a])
        return self.p[a]

    def union(self, a, b):
        a = self.get(a)
        b = self.get(b)
        if a == b: return
        if self.r[a] >= self.r[b]:
            self.p[a] = self.p[b]
        else:
            self.p[b] = self.p[a]
        self.r[a] = self.r[a] + self.r[b]
        self.r[b] = self.r[a]


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

