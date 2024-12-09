import sys, math
from collections import deque, defaultdict, Counter

MOD       = 10**9 + 7
INF       = float('inf')
NINF      = float('-inf')
YES, NO   = "YES", "NO"
MT        = False

def gcd_distinct(arr):
    M = -1
    gcds = set()
    N = len(arr)

    Mp = {}

    for i in range(N):
        M = max(M, arr[i])
        Mp[arr[i]] = 1

    for i in range(1, M + 1, 1):
        currGcd = 0

        for j in range(i, M + 1, i):
            if j in Mp:
                currGcd = math.gcd(currGcd, j)

                if currGcd == i:
                    gcds.add(currGcd)
                    break

    return list(gcds)

#---------------------------------------------------
def sol():
    n = ipt()
    a = ilist()
    l = set(a)
    a.sort()
    k = gcd_distinct(a)
    res = 0
    for i in k:
        if i not in l:
            res += 1
            l.add(i)
    print(res)

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

