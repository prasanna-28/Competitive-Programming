import sys, math
from collections import deque, defaultdict, Counter

MOD       = 10**9 + 7
INF       = float('inf')
NINF      = float('-inf')
YES, NO   = "YES", "NO"
MT        = True

#---------------------------------------------------
def sol():
    n = ipt()
    verts = {}
    adj = defaultdict(list)
    for i in range(n-1):
        u,v = ivars()
        verts[(u,v)] = i
        adj[u].append(v)
        adj[v].append(u)
    start = None
    for i in adj:
        if len(adj[i]) > 2:
            print(-1)
            return
        elif len(adj[i]) == 1:
            start = i

    seen = set()
    res = [0] * (n-1)
    curr = start

    two = False
    nxt = None

    for _ in range(n-1):
        seen.add(curr)
        for vertex in adj[curr]:
            if vertex not in seen:
                nxt = vertex
        if nxt in seen or nxt == None: break
        if (nxt, curr) in verts:
            if two:
                res[verts[(nxt, curr)]] = 2
            else:
                res[verts[(nxt, curr)]] = 3
        else:
            if two:
                res[verts[(curr, nxt)]] = 2
            else:
                res[verts[(curr, nxt)]] = 3
        two = not two
        curr = nxt
    print(ljoin(res))



#---------------------------------------------------
def main():
    for _ in range(ipt() if MT else 1): sol()

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
    main()

