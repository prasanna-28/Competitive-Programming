import sys, math
from collections import deque, defaultdict, Counter

MOD       = 10**9 + 7
INF       = float('inf')
NINF      = float('-inf')
YES, NO   = "YES", "NO"
MT        = 1

#---------------------------------------------------
def sol():
    zeros = set()
    res = set()
    n = ipt()
    a = ilist()
    b = len(bin(max(a))) - 1
    for i in a:
        j = 0
        for _ in range(b):
            if i & 1:
                res.add(2**j)
            else:
                zeros.add(2**j)
            j += 1
            i >>= 1
    tot = 0
    for i in res:
        if i in zeros:
            tot += i
    print(tot)

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

