import sys, math
from collections import deque, defaultdict, Counter

MOD       = 10**9 + 7
INF       = float('inf')
NINF      = float('-inf')
YES, NO   = "YES", "NO"
MT        = True

#---------------------------------------------------
def sol():
    n,m = ivars()
    grid = []
    for _ in range(n):
        s = list(input())
        grid.append(s)
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '#':
                start = (i, j)
                break
        else:
            continue
        break
    length = 0
    x,y = start

    while x < n and grid[x][y] == '#':
        x += 1
        length += 1
    print(start[0] + length // 2 + 1, start[1] + 1)


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

