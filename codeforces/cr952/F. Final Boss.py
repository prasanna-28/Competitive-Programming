import sys, math
from collections import deque, defaultdict, Counter

MOD       = 10**9 + 7
INF       = float('inf')
NINF      = float('-inf')
YES, NO   = "YES", "NO"
MT        = True

#---------------------------------------------------
def sol():
    h,n = ivars()
    a = ilist()
    c = ilist()
    ac = defaultdict(int)
    for i in range(n):
        ac[str(c[i])] += a[i]

    if sum(c) >= h:
        print(1)
        return
    h -= sum(c)
    turn = 1

    ac = [(key, ac[str(key)]) for key in set(c)]

    diff = [0] * (h + 1)
    for key, value in diff:
        for x in range(0, h + 1, key):
            if x == 0: continue
            diff[x] += value

    add = []
    for i,v in enumerate(diff):
        add.append((i, v))
    ld = h + 1

    while h > 0:





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

