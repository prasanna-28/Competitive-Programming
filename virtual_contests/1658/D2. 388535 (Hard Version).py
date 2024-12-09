import sys, math
from collections import deque, defaultdict, Counter

MOD       = 10**9 + 7
INF       = float('inf')
NINF      = float('-inf')
YES, NO   = "YES", "NO"
MT        = True

#---------------------------------------------------
def sol():
    l,r = ivars()
    a = ilist()
    for i in range(len(a)):
        a[i] -= l
    bits = [[0] * (r+1 - l) for _ in range(18)]
    for i in range(l, r+1):
        idx = i - l
        j = 0
        while i > 0:
            bits[j][idx] = i & 1
            i >>= 1
            j += 1
    bits2 = [[0] * (r+1 - l) for _ in range(18)]
    for i in range(len(a)):
        j = 0
        while a[i] > 0:
            bits2[j][i] = a[i] & 1
            a[i] >>= 1
            j += 1
    res = [0] * 18
    for i in range(18):
        if sum(bits[i]) != sum(bits2[i]):
            res[i] = 1
    res = ''.join(map(str, reversed(res)))
    print(int(res, 2) + l)


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

