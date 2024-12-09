import sys, math
from collections import deque, defaultdict, Counter

MOD       = 10**9 + 7
INF       = float('inf')
NINF      = float('-inf')
YES, NO   = "YES", "NO"
MT        = True

#---------------------------------------------------
def sol():
    res = []
    n = ipt()
    s = list(map(int, slist()))
    res.append(s.pop())
    ops = 0

    while len(s) > 0:
        curr = s.pop()
        if curr:
            res.append(curr)
        else:
            if not res[-1]:
                ops += 2
                res.append(1)
                res.append(1)
            elif len(res) > 1 and not res[-2]:
                ops += 1
                res.append(1)
            res.append(curr)
    print(ops)


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

