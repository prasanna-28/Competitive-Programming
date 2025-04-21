MOD = 10**9 + 7
MAXN = 5000

# Precompute factorial and inverse factorial modulo MOD
fact = [1] * (MAXN + 1)
inv_fact = [1] * (MAXN + 1)

for i in range(1, MAXN + 1):
    fact[i] = fact[i-1] * i % MOD

inv_fact[MAXN] = pow(fact[MAXN], MOD-2, MOD)
for i in range(MAXN-1, -1, -1):
    inv_fact[i] = inv_fact[i+1] * (i+1) % MOD

def C(n, k):
    if n < 0 or k < 0 or k > n:
        return 0
    return fact[n] * inv_fact[k] % MOD * inv_fact[n - k] % MOD

def solve():
    import sys
    input = sys.stdin.read().split()
    idx = 0
    t = int(input[idx])
    idx += 1
    for _ in range(t):
        n = int(input[idx])
        idx += 1
        a = list(map(int, input[idx:idx+n]))
        idx += n
        
        fixed = {}
        missing_pos = []
        present = set()
        for i in range(n):
            if a[i] != -1:
                present.add(a[i])
                fixed[a[i]] = i
            else:
                missing_pos.append(i)
        m = len(missing_pos)
        missing_nums = set()
        for x in range(n):
            if x not in present:
                missing_nums.add(x)
        
        ans = 0
        
        for j in range(n + 1):
            fixed_cnt = sum(1 for x in present if x < j)
            s = j - fixed_cnt
            if s < 0 or s > m:
                continue
            
            required_missing = sum(1 for x in missing_nums if x < j)
            if required_missing != s:
                continue
            
            if j in present:
                j_pos = fixed[j]
                fixed_under_j = [fixed[x] for x in present if x < j]
                if not fixed_under_j:
                    L_min, R_max = -1, -1
                else:
                    L_min = min(fixed_under_j)
                    R_max = max(fixed_under_j)
                
                if fixed_under_j and (L_min <= j_pos <= R_max):
                    continue
                
                if not fixed_under_j:
                    L_options = j_pos + 1
                    R_options = n - j_pos
                else:
                    if j_pos < L_min:
                        L_options = j_pos + 1
                        R_options = n - R_max
                    else:  # j_pos > R_max
                        L_options = L_min + 1
                        R_options = n - j_pos
                
                ways_LR = L_options * R_options % MOD
                
                if s == 0:
                    perm_ways = fact[m]
                else:
                    perm_ways = C(m, s) * fact[s] % MOD * fact[m-s] % MOD
                
                ans_j = ways_LR * perm_ways % MOD
                ans_j = ans_j * j % MOD
                ans = (ans + ans_j) % MOD
            else:
                if s == 0:
                    continue
                
                fixed_under_j = [fixed[x] for x in present if x < j]
                
                if fixed_under_j:
                    L_min = min(fixed_under_j)
                    R_max = max(fixed_under_j)
                else:
                    L_min = n
                    R_max = -1
                
                PF = [0]*(n+1)
                for i in range(n):
                    PF[i+1] = PF[i] + (a[i] == -1)
                
                total = 0
                for R in range(n):
                    for L in range(R + 1):
                        if fixed_under_j:
                            if L > L_min or R < R_max:
                                continue
                        if j < n and j in fixed and L <= fixed[j] <= R:
                            continue
                        k = PF[R+1] - PF[L]
                        if k < s:
                            continue
                        comb = C(k, s) * fact[s] % MOD
                        rem = m - s
                        comb = comb * C(rem, k - s) % MOD
                        comb = comb * fact[k - s] % MOD
                        comb = comb * fact[rem - (k - s)] % MOD
                        total = (total + comb) % MOD
                ans = (ans + total * j % MOD) % MOD
        
        print(ans % MOD)

solve()
