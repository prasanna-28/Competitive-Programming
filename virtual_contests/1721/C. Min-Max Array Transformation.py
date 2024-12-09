import sys, math
from collections import deque, defaultdict, Counter
from bisect import bisect_left, bisect_right

MOD       = 10**9 + 7
INF       = float('inf')
NINF      = float('-inf')
YES, NO   = "YES", "NO"
MT        = True

#---------------------------------------------------
def sol():
    n = ipt()
    a = ilist()
    b = ilist()
    # for biggest, any time bisect_left == index, pop until index
    # otherwise take last one in the queue (biggest) and subtract the current index from it
    q = b[:]
    i = n - 1
    dmax = [0] * n
    dmin = [0] * n
    while i >= 0:
        curr = bisect_left(q, a[i])
        dmax[i] = q[-1] - a[i]
        dmin[i] = q[curr] - a[i]
        if curr == i:
            while len(q) > curr:
                q.pop()
        i -= 1
    print(ljoin(dmin))
    print(ljoin(dmax))


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

