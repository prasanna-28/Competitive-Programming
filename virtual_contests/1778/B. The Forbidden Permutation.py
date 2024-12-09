import sys, math
from collections import deque, defaultdict, Counter

MOD       = 10**9 + 7
INF       = float('inf')
NINF      = float('-inf')
YES, NO   = "YES", "NO"
MT        = True

#---------------------------------------------------
def sol():
    n, m, d = ivars()
    p = ilist()
    a = ilist()
    idx = {}
    for i,v in enumerate(p):
        idx[v] = i
    res = INF
    for i in range(m-1):
        k = idx[a[i+1]] - idx[a[i]]
        k = d - k + 1
        diff = idx[a[i]] + (n - idx[a[i + 1]] - 1)
        if diff < k:
            k = INF
        res = min(res, idx[a[i+1]] - idx[a[i]], k)
    print(max(res, 0))


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

