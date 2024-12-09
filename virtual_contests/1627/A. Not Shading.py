import sys, math
from collections import deque, defaultdict, Counter

MOD       = 10**9 + 7
INF       = float('inf')
NINF      = float('-inf')
YES, NO   = "YES", "NO"
MT        = True

#---------------------------------------------------
def sol():
    n,m,r,c = ivars()
    grid = []
    for i in range(n):
        a = input()
        k = []
        for i in a:
            if i == 'W':
                k.append(0)
            else:
                k.append(1)
        grid.append(k)
    r -= 1
    c -= 1
    if grid[r][c]:
        print(0)
        return
    for i in range(n):
        if grid[i][c]:
            print(1)
            return
    for j in range(m):
        if grid[r][j]:
            print(1)
            return
    if sum([sum(a) for a in grid]) > 0:
        print(2)
        return
    print(-1)


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

