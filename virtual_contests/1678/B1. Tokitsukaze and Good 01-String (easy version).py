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
    b = slist()
    l = []
    i = 0
    while i < n:
        curr = b[i]
        length = 0
        while i < n and b[i] == curr:
            i += 1
            length += 1
        l.append(length)
    i = 0
    ops = 0
    while i < len(l)-1:
        if l[i] % 2 == 1:
            l[i] -= 1
            l[i+1] += 1
            ops += 1
        i += 1
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

