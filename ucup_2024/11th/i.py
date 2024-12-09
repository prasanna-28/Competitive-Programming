import sys
def main():
    MOD = 998244353

    N_and_rest = sys.stdin.read().split()
    N = int(N_and_rest[0])
    A = list(map(int, N_and_rest[1:N+1]))
    S = sum(A)

    if S % 2 != 0:
        print(0)
        return
    target = S // 2

    dp = [ [0]*(target+1) for _ in range(N+1)]
    dp[0][0] = 1

    for a in A:
        for i in range(N, 0, -1):
            for s in range(target, a-1, -1):
                dp[i][s] = (dp[i][s] + dp[i-1][s - a]) % MOD

    fact = [1]*(N+1)
    for i in range(1,N+1):
        fact[i] = (fact[i-1] * i) % MOD

    ans = 0
    for i in range(1,N):
        if target <= S and target >=0 and dp[i][target]:
            term = (dp[i][target] * fact[i]) % MOD
            term = (term * fact[N-i]) % MOD
            ans = (ans + term) % MOD

    print(ans)

if __name__ == "__main__":
    main()

