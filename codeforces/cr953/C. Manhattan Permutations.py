import sys, math
from collections import deque, defaultdict, Counter

MOD       = 10**9 + 7
INF       = float('inf')
NINF      = float('-inf')
YES, NO   = "YES", "NO"
MT        = True

#---------------------------------------------------
def sol():
    n,k = ivars()
    s = 0
    for i in range(1, n + 1):
        s += abs(i - (n + 1 - i))
    if k > s or (s - k) & 1:
        print('No')
        return
    res = list(range(1, n + 1))
    l = 0
    r = n - 1
    p = 0
    while l < r:
        if p == k: break
        if p + 2 * (res[r] - res[l]) > k:
            l += 1
            continue
        p += 2 * (res[r] - res[l])
        res[l], res[r] = res[r], res[l]
        l += 1
        r -= 1
    print('Yes')
    print(ljoin(res))


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

