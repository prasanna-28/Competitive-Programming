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
    h = ilist()
    p = ilist()
    hp = list(zip(h,p))
    hp.sort(key = lambda x: x[1])

    currsum = 0

    for h,p in hp:
        if h <= currsum: continue
        oh = h
        if k <= 0:
            print(NO)
            return
        if (h,p) != hp[0]:
            k -= p
            if k <= 0:
                print(NO)
                return
        h = h - currsum
        while h > 0:
            h -= k
            if h <= 0: break
            k -= p
            if k < 0:
                print(NO)
                return
        currsum = oh - h
    print(YES if k >= 0 else NO)

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

