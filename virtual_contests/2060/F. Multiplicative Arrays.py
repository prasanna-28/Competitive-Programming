import sys
input_data = sys.stdin.read().strip().split()
t = int(input_data[0])
MOD = 998244353

tests = []
ptr = 1
max_k = 0
max_n = 0
for _ in range(t):
    kk = int(input_data[ptr]); nn = int(input_data[ptr+1])
    ptr += 2
    tests.append((kk, nn))
    if kk > max_k:
        max_k = kk
    if nn > max_n:
        max_n = nn

A = [0]*(max_k+1)
for i in range(1, max_k+1):
    A[i] = 1

E = [0]*(max_k+1)
E[1] = 1

def dirichlet_convolution(f, g, k):
    h = [0]*(k+1)
    for i in range(1, k+1):
        fi = f[i]
        if fi != 0:
            multiple = i
            step = i
            while multiple <= k:
                h[multiple] = (h[multiple] + fi*g[multiple//i]) % MOD
                multiple += step
    return h

def add_arrays(f, g, k):
    return [(f[i] + g[i]) % MOD for i in range(k+1)]

def sub_arrays(f, g, k):
    return [(f[i] - g[i]) % MOD for i in range(k+1)]

def combine_pairs(B1, S1, B2, S2, k):
    newB = dirichlet_convolution(B1, B2, k)
    S2_minus_E = sub_arrays(S2, E, k)
    tmp = dirichlet_convolution(B1, S2_minus_E, k)
    newS = add_arrays(S1, tmp, k)
    return (newB, newS)


maxP = max_n.bit_length()
Bpow = [None]*(maxP+1)
Spow = [None]*(maxP+1)

Bpow[0] = A[:]
Spow[0] = add_arrays(E, A, max_k)

for p in range(1, maxP):
    Bp_1 = Bpow[p-1]
    Bpow[p] = dirichlet_convolution(Bp_1, Bp_1, max_k)
    Sp_1 = Spow[p-1]
    S_2p = None
    (newB, newS) = combine_pairs(Bp_1, Sp_1, Bp_1, Sp_1, max_k)
    Bpow[p] = newB
    Spow[p] = newS


def get_BS_of_n(n, k):
    curB = E[:]
    curS = E[:]
    shift = 0
    tmp_n = n
    while tmp_n > 0:
        if (tmp_n & 1):
            (curB, curS) = combine_pairs(curB, curS, Bpow[shift], Spow[shift], k)
        tmp_n >>= 1
        shift += 1
    return (curB, curS)


out = []
pos = 0
for (k_i, n_i) in tests:
    if n_i < 1:
        ans = ["0"] * k_i
        out.append(" ".join(ans))
        continue

    (Bn, Sn) = get_BS_of_n(n_i, k_i)
    res = [0]*k_i
    for x in range(1, k_i+1):
        val = Sn[x]
        if x == 1:
            val = (val - 1) % MOD
        res[x-1] = str(val % MOD)
    out.append(" ".join(res))

print("\n".join(out))

