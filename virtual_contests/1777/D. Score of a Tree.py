import sys, math
from collections import deque, defaultdict, Counter

MOD       = 10**9 + 7
INF       = float('inf')
NINF      = float('-inf')
YES, NO   = "YES", "NO"
MT        = True

sys.setrecursionlimit(2 * 10**5 + 1)
#---------------------------------------------------
def sol():
    n = ipt()
    adj = defaultdict(list)
    for i in range(n-1):
        u,v = ivars()
        adj[u].append(v)
        adj[v].append(u)
    leaf_nodes = []
    for i in range(1, n+1):
        if len(adj[i]) == 1:
            leaf_nodes.append(i)

    heights = [0] * (n+1)

    def bfs(parent, child):
        heights[child] = 1
        for node in adj[child]:
            if node != parent:
                bfs(child, node)
                heights[child] = max(heights[child]  , heights[node] + 1)
    bfs(0, 1)

    print(max(sum(heights) * pow(2, n-1, MOD) % MOD, 1))
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

