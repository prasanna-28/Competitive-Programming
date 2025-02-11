import sys

input_data = sys.stdin.read().strip().split()
t = int(input_data[0])
ptr = 1

def solve_one_test(n, arr):
    res = 0
    for length in range(1, n+1, 2):
        res += (n - length + 1)

    for m in range(1, 11):
        ps = [0]*(n+1)
        pl = [0]*(n+1)
        pe = [0]*(n+1)
        for i in range(n):
            ps[i+1] = ps[i] + (1 if arr[i] <= m else 0)
            pl[i+1] = pl[i] + (1 if arr[i] >= m else 0)
            pe[i+1] = pe[i] + (1 if arr[i] == m else 0)
        S = [0]*(n+1)
        T = [0]*(n+1)
        for i in range(n+1):
            S[i] = ps[i] - (i//2)
            T[i] = pl[i] - (i//2)

        even_indices = []
        odd_indices = []
        for i in range(n+1):
            if i % 2 == 0:
                even_indices.append(i)
            else:
                odd_indices.append(i)

        extra_count = 0
        def check_subarray(L, R):
            length = R - L
            if length % 2 != 0:
                return 0
            half = length // 2
            sm = ps[R] - ps[L]
            lg = pl[R] - pl[L]
            eq = pe[R] - pe[L]
            if sm >= (half+1) and lg >= (half+1) and eq >= 2:
                return 1
            return 0

        for parity_list in (even_indices, odd_indices):
            for i1 in range(len(parity_list)):
                L = parity_list[i1]
                for i2 in range(i1+1, len(parity_list)):
                    R = parity_list[i2]
                    extra_count += check_subarray(L, R)

        res += extra_count

    return res

answers = []
for _ in range(t):
    n = int(input_data[ptr]); ptr += 1
    arr = list(map(int, input_data[ptr:ptr+n]))
    ptr += n
    ans = solve_one_test(n, arr)
    answers.append(ans)

print('\n'.join(map(str, answers)))

