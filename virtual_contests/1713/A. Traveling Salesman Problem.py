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
    ys = [0]
    nys = [0]
    xs = [0]
    nxs = [0]
    for _ in range(n):
        x,y = ivars()
        if x < 0:
            nxs.append(abs(x))
        if x > 0:
            xs.append(abs(x))
        if y < 0:
            nys.append(abs(y))
        if y > 0:
            ys.append(y)
    res = 0
    for i in [ys, nys, xs, nxs]:
        res += max(i)
    print(res*2)
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

