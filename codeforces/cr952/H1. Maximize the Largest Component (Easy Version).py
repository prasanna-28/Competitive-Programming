import sys, math
from collections import deque, defaultdict, Counter
sys.setrecursionlimit(10000)
MOD       = 10**9 + 7
INF       = float('inf')
NINF      = float('-inf')
YES, NO   = "YES", "NO"
MT        = True
out = []

#---------------------------------------------------
def sol():
    n,m = ivars()

    grid = []
    for _ in range(n):
        grid.append([1 if i == '#' else 0 for i in input()])
    if n == 1 or m == 1:
        out.append(n * m)
        return

    dsu = DSU(n * m)

    for i in range(n):
        for j in range(m):
            if grid[i][j]:
                if i + 1 < n and grid[i+1][j]:
                    dsu.union(i * m + j, (i + 1) * m + j)
                if j + 1 < m and grid[i][j+1]:
                    dsu.union(i * m + j, i * m + j + 1)
    res = 0

    for i in range(n):
        for j in range(m):
            if grid[i][j]:
                grid[i][j] = dsu.get(i*m + j)
            else:
                grid[i][j] = -1
    prev = set()
    for row in range(n):
        checked = set()
        curr = 0
        currset = set()
        for j in range(m):
            if grid[row][j] > -1 and (u:=grid[row][j]) not in checked:
                curr += (dsu.r[u])
                checked.add(u)
                currset.add(u)
            elif grid[row][j] < 0:
                curr += 1
        for i in prev:
            if i not in checked:
                curr += (dsu.r[i])
                checked.add(i)
        if row < n - 1:
            row += 1
            for j in range(m):
                if grid[row][j] > -1 and (u:=grid[row][j]) not in checked:
                    curr += (dsu.r[u])
                    checked.add(u)
        res = max(res, curr)
        prev = currset

    prev = set()

    for col in range(m):
        checked = set()
        curr = 0
        currset = set()
        for i in range(n):
            if grid[i][col] > -1 and (u:=grid[i][col]) not in checked:
                curr += dsu.r[u]
                checked.add(u)
                currset.add(u)
            elif grid[i][col] == -1:
                curr += 1
        for i in prev:
            if i not in checked:
                curr += dsu.r[i]
                checked.add(i)
        if col < m - 1:
            col += 1
            for i in range(n):
                if grid[i][col] > 0 and (u:=grid[i][col]) not in checked:
                    curr += dsu.r[u]
                    checked.add(u)
        res = max(res, curr)
        prev = currset

    out.append(res)


#---------------------------------------------------

class DSU:
    def __init__(self, n):
        self.p = [i for i in range(n)]
        self.r = [1 for _ in range(n)]

    def get(self, a):
        if self.p[a] != a:
            self.p[a] = self.get(self.p[a])
        return self.p[a]

    def union(self, a, b):
        a = self.get(a)
        b = self.get(b)
        if a == b: return
        if self.r[a] <= self.r[b]:
            self.p[a] = self.p[b]
            self.r[b] += self.r[a]
        else:
            self.p[b] = self.p[a]
            self.r[a] += self.r[b]


def main():
    for _ in range(ipt() if MT else 1): sol()
    print(njoin(map(str, out)))

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
