import   sys, math
from collections import deque
finp   = sys.stdin.readline
MOD    = 10**9 + 7
njoin  = lambda x: '\n'.join(map(str, x))
ljoin  = lambda x: ' '.join(map(str, x))
sjoin  = lambda x: '\n'.join(x)
initl  = lambda x,y: [y]*x
INF    = float('inf')
NINF   = float('-inf')
ilist  = lambda: list(map(int, finp().split()))
slist  = lambda: list(input())
slists = lambda: input().split()
ivars  = lambda: map(int, finp().split())
ipt    = lambda: int(finp())
out    = []
#=============================================#
def sol():
    n,m = ivars()
    grid = []


def sol4():
    n,m = ivars()
    dp = [[0]*m for _ in range(n)]
    dp[-1][-1] = -grid[-1][-1]
    for i in range(m-1, -1, -1):
        dp[-1][i] = dp[-1][i+1] - grid[-1][i]
    for i in range(n-1, -1, -1):
        dp[i][-1] = dp[i+1][-1] - grid[i][-1]
    for i in range(n-1, -1, -1):
        for j in range(m-1, -1, -1):
            pass


def sol3():
    n,m = ivars()
    grid = []
    for _ in range(n):
        grid.append(ilist())
    dp = [[set() for _ in range(n)] for _ in range(m)]
    for i in range(n):
        dp[0][i].add(grid[0][i])
    for i in range(m):
        dp[i][0].add(grid[i][0])

def sol2():
    n,m = ivars()
    grid = []
    for _ in range(n):
        grid.append(ilist())
    end = (n-1, m-1)
    poss = False
    Q = deque([(0,0,grid[0][0])])
    while len(Q) > 0:
        x,y,score = Q.popleft()
        if (x,y) == end:
            poss = score == 0
            if poss: break
            continue
        if x < n-1:
            Q.append((x+1, y, score + grid[x+1][y]))
        if y < m - 1:
            Q.append((x, y+1, score + grid[x][y+1]))
    print("YES" if poss else "NO")






#=============================================#
def bellman_ford(grid):
    m, n = len(grid), len(grid[0])
    dist = [[float('inf')] * n for _ in range(m)]
    dist[0][0] = 0

    for _ in range(m + n - 1):
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                if i > 0:
                    dist[i][j] = min(dist[i][j], dist[i-1][j] + grid[i][j])
                if j > 0:
                    dist[i][j] = min(dist[i][j], dist[i][j-1] + grid[i][j])
    for i in dist:
        print(i)
    return abs(dist[m-1][n-1])

if __name__ == "__main__":
    for _ in range(ipt()): sol()
    #sol()
    pass



