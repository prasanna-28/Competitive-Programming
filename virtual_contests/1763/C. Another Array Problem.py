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
    a = ilist()

    if n == 2:
        print(max(sum(a), abs(a[0] - a[1]) * 2))
        return

    if n == 3:
        poss = [sum(a), a[0] * 3, a[-1] * 3, abs(a[0] - a[1]) * 3, abs(a[1] - a[2]) * 3, abs(a[1] - a[2]) * 3]
        print(max(poss))
        return

    print(max(a) * n)
    return

    assert(0)


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

