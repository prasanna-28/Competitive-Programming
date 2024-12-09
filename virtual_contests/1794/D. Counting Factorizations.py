import sys, math
from collections import deque, defaultdict, Counter

MOD       = 998_244_353
INF       = float('inf')
NINF      = float('-inf')
YES, NO   = "YES", "NO"
MT        = False
N_MAX     = (2022 << 2) + 5

factorials = [1]
I = 1
while len(factorials) <= N_MAX:
    factorials.append((factorials[-1] * I) % MOD)
    I += 1

#---------------------------------------------------
def sol():
    n = ipt()
    a = ilist()
    primes = []
    composites = []
    k = Counter(a)
    for i in a:
        if i == 1:
            composites.append(i)
            continue
        for f in range(2, math.isqrt(i) + 1):
            if i%f == 0:
                composites.append(i)
                break
        else:
            primes.append(i)

    s_primes = list(set(primes))

    if len(s_primes) < n:
        print(0)
        return

    dp = [[0] * (n+1) for _ in range(len(s_primes))]
    dp[0][0] = pow(factorials[k[s_primes[0]]], -1, MOD)
    dp[0][1] = pow(factorials[k[s_primes[0]] - 1], -1, MOD)
    for i in range(1, len(s_primes)):
        for j in range(n + 1):
            if j > 0:
                dp[i][j] += dp[i-1][j-1] * pow(factorials[k[s_primes[i]] - 1], -1, MOD)
            dp[i][j] += dp[i-1][j] * pow(factorials[k[s_primes[i]]], -1, MOD)
            dp[i][j] %= MOD

    C = dp[-1][-1]
    res = (factorials[n] * C) % MOD
    for i in set(composites):
        res = (res * pow(factorials[k[i]], -1, MOD)) % MOD

    print(res)



    # dp[i][j]
    # choose which prime in factors
    # prime in factor -> multiply by 1/(c-1)
    # prime not in factor -> multiply by 1/c
    # dp[i][j] -> ith prime, j have been chosen
    # dp[i][j] = dp[i-1][j] * (1/c) + dp[i-1][j-1] * 1/(c-1)
    # where c is the number of times that prime appears
    # dp[-1][-1] will hold answer






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

