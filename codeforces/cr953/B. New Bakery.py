import sys, math
from collections import deque, defaultdict, Counter

MOD       = 10**9 + 7
INF       = float('inf')
NINF      = float('-inf')
YES, NO   = "YES", "NO"
MT        = True

#---------------------------------------------------
'''
b + b - 1 + b - 2 + ... + b - (k - 1)
kb - (sum[1..k-1])
'''
def sol():
    n,a,b = ivars()
    left = 0
    right = min(n, b)
    def cond(k):
        an = n - k
        l = k*b - (k * (k-1))//2
        r = a * an
        return l + r
    res = ternary_search_peak(cond, left, right)
    print(res)

def ternary_search_peak(cond, left, right):
    if left == right:
        return cond(left)

    if right == left + 1:
        return max(cond(left), cond(right))

    mid1 = left + (right - left) // 3
    mid2 = right - (right - left) // 3

    if cond(mid1) > cond(mid2):
        return ternary_search_peak(cond, left, mid2 - 1)
    else:
        return ternary_search_peak(cond, mid1 + 1, right)

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

