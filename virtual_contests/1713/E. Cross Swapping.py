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
    grid = [[] for _ in range(n)]
    for i in range(n):
        grid[i] = ilist()
    for i in range(n):
        for j in range(i+1, n):
            if grid[j][i] < grid[i][j]:
                print((i, j))
                grid[j][i], grid[i][j] = grid[i][j], grid[j][i]
    for i in grid:
        print(ljoin(i))



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

