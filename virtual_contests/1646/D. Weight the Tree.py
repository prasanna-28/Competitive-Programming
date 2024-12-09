import sys
import math
from collections import deque, defaultdict, Counter, OrderedDict

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
    n = ipt()
    adj = defaultdict(list)
    res = [0] * (n+1)
    for _ in range(n-1):
        u,v = ivars()
        adj[u].append(v)
        adj[v].append(u)
    seen = set()
    good = 0
    for val in sorted(adj.keys(), key = lambda x: len(adj[x])):
        if val in seen: continue
        seen.add(val)
        good += 1
        res[val] = len(adj[val])
        for v in adj[val]:
            if len(adj[val]) == 1 and len(adj[v]) == 1: good += 1
            res[v] = 1
            seen.add(v)
    print(good, sum(res))
    print(ljoin(res[1:]))

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

