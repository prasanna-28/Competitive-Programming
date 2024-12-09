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
    dists = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            dists[i][j] = max(i + j, abs(n - i - 1) + abs(m-j-1), abs(n-1-i) + j, i + abs(m-j-1))
    dists = [x for xs in dists for x in xs]
    dists.sort()
    print(ljoin(dists))



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

