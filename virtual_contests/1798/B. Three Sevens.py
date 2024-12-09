import sys, math
from collections import deque, defaultdict, Counter

MOD       = 10**9 + 7
INF       = float('inf')
NINF      = float('-inf')
YES, NO   = "YES", "NO"
MT        = True

#---------------------------------------------------
def sol():
    m = ipt()
    ns = []
    for _ in range(m):
        n = ipt()
        a = ilist()
        ns.append(a)
    ns.reverse()
    seen = set()
    res = []
    for day in ns:
        for k in day:
            if k not in seen:
                res.append(k)
                break
        else:
            print(-1)
            return
        for k in day:
            seen.add(k)
    print(ljoin(reversed(res)))



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

