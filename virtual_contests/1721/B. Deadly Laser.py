import sys, math
from collections import deque, defaultdict, Counter

MOD       = 10**9 + 7
INF       = float('inf')
NINF      = float('-inf')
YES, NO   = "YES", "NO"
MT        = True

def dist(a, b):
    ax, ay = a
    bx, by = b
    return abs(ax - bx) + abs(ay - by)
#---------------------------------------------------
def sol():
    n,m,sx,sy,d = ivars()
    res = n + m - 2
    top, bottom, left, right = False, False, False, False
    for i in range(1, n+1):
        if dist((i, m), (sx, sy)) <= d:
            right = True
        if dist((i, 1), (sx, sy)) <= d:
            left = True
    for i in range(1, m+1):
        if dist((n, i), (sx, sy)) <= d:
            bottom = True
        if dist((1, i), (sx, sy)) <= d:
            top = True


    if (right and bottom) or (top and left) or (top and bottom) or (right and left):
        print(-1)
        return
    print(res)


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

