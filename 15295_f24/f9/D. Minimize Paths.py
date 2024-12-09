import sys
MOD = 10**9 + 7

def main():
    n, k = map(int, sys.stdin.readline().split())

    MAX_N = 2 * n + 10
    factorials = [1] * (MAX_N)
    inv_factorials = [1] * (MAX_N)

    for i in range(1, MAX_N):
        factorials[i] = (factorials[i - 1] * i) % MOD

    inv_factorials[MAX_N - 1] = pow(factorials[MAX_N - 1], MOD - 2, MOD)
    for i in range(MAX_N - 2, -1, -1):
        inv_factorials[i] = inv_factorials[i + 1] * (i + 1) % MOD

    def comb(n, r):
        if r < 0 or r > n:
            return 0
        return factorials[n] * inv_factorials[r] % MOD * inv_factorials[n - r] % MOD

    answers = []
    have = k - 1
    for i in range(n + 1):
        if i == 0:
            answers.append(0)
            continue
        blocks = n - i - 1
        curr = comb(blocks- 1, have-1) * (blocks) + comb(blocks, have) + comb(blocks, have)
        answers.append(curr % MOD)
    answers[0] = (comb((2 * n)- 2, k) - sum(answers)) % MOD
    print(' '.join(map(str, answers)))

main()
