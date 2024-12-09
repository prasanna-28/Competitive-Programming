import sys, math
from collections import deque, defaultdict, Counter
def sieve(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    primes = [i for i in range(n + 1) if is_prime[i]]
    return set(primes)
MOD       = 998244353
INF       = float('inf')
NINF      = float('-inf')
YES, NO   = "YES", "NO"
MT        = True
PRIMES    = sieve(1001) | set([1])
#---------------------------------------------------
def sol():
    n = ipt()
    if n % 2:
        print(0)
        return
    res = 1
    k = n//2
    for i in range(1, k+1):
        res *= (i*i)
        res %= MOD
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

