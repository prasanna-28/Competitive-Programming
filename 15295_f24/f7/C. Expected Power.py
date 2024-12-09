MOD = 10**9 + 7
import sys
def main():
    t = int(sys.stdin.readline())
    max_n = 200000
    inv10000 = pow(10000, MOD-2, MOD)
    inv10000_pow = [1] * (max_n +1)
    for k in range(1, max_n +1):
        inv10000_pow[k] = inv10000_pow[k-1] * inv10000 % MOD
    pair_list = []
    pair_map = {}
    idx =0
    for b in range(10):
        for c in range(b+1,10):
            pair_list.append( (b,c) )
            pair_map[(b,c)] = idx
            idx +=1
    inv2 = pow(2, MOD-2, MOD)
    inv4 = pow(4, MOD-2, MOD)
    pow2 = [1] * 21
    for k in range(1,21):
        pow2[k] = pow2[k-1] *2 % MOD
    for _ in range(t):
        n = int(sys.stdin.readline())
        a = list(map(int, sys.stdin.readline().split()))
        p = list(map(int, sys.stdin.readline().split()))
        bits_set = [[] for _ in range(10)]
        list_bc = [[] for _ in range(45)]
        for i in range(n):
            bits = []
            ai = a[i]
            for b in range(10):
                if (ai >> b) &1:
                    bits.append(b)
                    bits_set[b].append(i)
            for j in range(len(bits)):
                for k in range(j+1, len(bits)):
                    b = bits[j]
                    c = bits[k]
                    idx_pair = pair_map[(b,c)]
                    list_bc[idx_pair].append(i)
        P_b = [1] *10
        for b in range(10):
            numerator_b =1
            for i in bits_set[b]:
                term = (10000 - 2 * p[i]) % MOD
                numerator_b = numerator_b * term % MOD
            cnt_b = len(bits_set[b])
            if cnt_b ==0:
                P_b[b] =1
            else:
                P_b[b] = numerator_b * inv10000_pow[cnt_b] % MOD
        E_X_b = [ ( (1 - P_b[b]) % MOD ) * inv2 % MOD for b in range(10)]
        list_bc_P = [1] *45
        for idx in range(45):
            lst = list_bc[idx]
            if len(lst) ==0:
                list_bc_P[idx] =1
            else:
                numerator_bc =1
                for i in lst:
                    term = (10000 - 2 * p[i]) % MOD
                    numerator_bc = numerator_bc * term % MOD
                cnt_bc = len(lst)
                list_bc_P[idx] = numerator_bc * inv10000_pow[cnt_bc] % MOD
        list_e_bxc = [0] *45
        for idx in range(45):
            b,c = pair_list[idx]
            P_b_current = P_b[b]
            P_c_current = P_b[c]
            P_bc_current = list_bc_P[idx]
            if P_bc_current !=0:
                inv_P_bc = pow(P_bc_current, MOD-2, MOD)
                term = P_b_current * P_c_current % MOD
                term = term * inv_P_bc % MOD
                term = term * inv_P_bc % MOD
            else:
                term =0
            e_bxc = (1 - P_b_current - P_c_current + term) % MOD
            e_bxc = e_bxc * inv4 % MOD
            list_e_bxc[idx] = e_bxc
        sum1 =0
        for b in range(10):
            sum1 = (sum1 + pow(4, b, MOD) * E_X_b[b])  % MOD
        sum2 =0
        for idx in range(45):
            b,c = pair_list[idx]
            sum2 = (sum2 + 2 * pow(2, b +c, MOD) * list_e_bxc[idx] ) % MOD
        E_X2 = (sum1 + sum2) % MOD
        print(E_X2)
if __name__ == "__main__":
    main()

