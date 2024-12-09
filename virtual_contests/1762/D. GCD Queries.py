import sys, math
from collections import deque, defaultdict, Counter

MOD       = 10**9 + 7
INF       = float('inf')
NINF      = float('-inf')
YES, NO   = "YES", "NO"
MT        = True

def query(x, y):
    print("?", x, y, flush = True)
    return int(input())

def answer(x, y):
    print("!", x, y, flush = True)
    if int(input()) < 0:
        exit(0)

#---------------------------------------------------
def sol():
    n = ipt()
    if n == 2:
        answer(1, 2)
        return
    i = 1
    j = 2
    k = 3
    nxt = 4
    not_zero = []
    while len(not_zero) < n - 2:
        l = query(i, k)
        r = query(k, j)
        if l == r:
            not_zero.append(k)
            k = nxt
        elif l < r:
            not_zero.append(i)
            i = nxt
        else:
            not_zero.append(j)
            j = nxt
        nxt += 1
    nz = set(not_zero)
    res = []
    for i in range(1, n + 1):
        if i not in nz:
            res.append(i)
    answer(*res)

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

