import sys, math
from collections import deque, defaultdict, Counter

MOD       = 10**9 + 7
INF       = float('inf')
NINF      = float('-inf')
YES, NO   = "YES", "NO"
MT        = True
factorials = [1]
for i in range(1, 100002):
    factorials.append((factorials[-1] * i) % MOD)

#---------------------------------------------------
def sol():
    n = ipt()
    res = 0
    for i in range(1, n + 1):
        res += (i-1)*2
        res %= MOD
    print((res * factorials[n]) % MOD)


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

