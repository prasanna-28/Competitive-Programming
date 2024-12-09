import sys
import threading

MOD = 998244353

def main():
    import sys
    from collections import defaultdict

    input = sys.stdin.read
    data = input().split()
    idx = 0
    t = int(data[idx]); idx +=1

    max_n = 2 * 10**5 + 10
    fact = [1]*(max_n)
    for i in range(1, max_n):
        fact[i] = fact[i-1]*i % MOD
    inv_fact = [1]*(max_n)
    inv_fact[max_n-1] = pow(fact[max_n-1], MOD-2, MOD)
    for i in range(max_n-2, -1, -1):
        inv_fact[i] = inv_fact[i+1]*(i+1)%MOD

    def comb(n, k):
        if n < k or k <0:
            return 0
        return fact[n]*inv_fact[k]%MOD * inv_fact[n-k]%MOD

    pow2 = [1]*(max_n)
    for i in range(1, max_n):
        pow2[i] = pow2[i-1]*2%MOD

    for _ in range(t):
        n = int(data[idx]); idx +=1
        a = list(map(int, data[idx:idx+n])); idx +=n
        cnt = defaultdict(int)
        for num in a:
            cnt[num] +=1
        m = max(cnt.keys(), default=-1)
        # Precompute 2^c[x] for all x
        two_pow = {}
        for x in cnt:
            two_pow[x] = pow2[cnt[x]]
        # Precompute sum of c[x} for x >=k
        sum_c = [0]*(m+2)
        for k in range(m, -1, -1):
            sum_c[k] = sum_c[k+1] + cnt.get(k,0)
        # Precompute 2^{sum_c[k}} for all k
        suffix_pow2 = [1]*(m+2)
        for k in range(m, -1, -1):
            suffix_pow2[k] = pow2[cnt.get(k,0)] * suffix_pow2[k+1] % MOD
        # Now, iterate over k from1 to m+1
        total =0
        # To optimize, precompute for each k, the product over x <k of (2^{c[x}} -1)
        # Initialize product
        prefix_product =1
        for k in range(1, m+2):
            valid = True
            term =1
            for x in range(0, k):
                if cnt.get(x,0) <1:
                    valid=False
                    break
                term = term * (two_pow[x] -1) % MOD
            if valid:
                N_k = term * suffix_pow2[k] % MOD
                total = (total + k * N_k) % MOD
        print(total)

threading.Thread(target=main).start()
