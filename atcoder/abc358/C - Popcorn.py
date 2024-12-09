import sys, math
from collections import deque, defaultdict, Counter
from itertools import combinations

MOD       = 10**9 + 7
INF       = float('inf')
NINF      = float('-inf')
YES, NO   = "YES", "NO"
MT        = False

#---------------------------------------------------
def sol():
    n, m = ivars()
    a = []
    for _ in range(n):
        x = input()
        ai = 0
        for i in range(m):
            if x[i] == 'o':
                ai |= (1<<i)
        a.append(ai)

    target = (1<<m) - 1

    for i in range(1, m + 1):
        for k in combinations(a, i):
            curr = 0
            for x in k:
                curr |= x
            if curr == target:
                print(i)
                return
    assert(False)


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

