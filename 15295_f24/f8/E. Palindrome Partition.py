import sys

def main():
    def manacher_even(s):
        n = len(s)
        d_even = [0] * n
        l, r = 0, -1

        for i in range(n):
            if i > r:
                k = 0
            else:
                k = min(d_even[l + r - i + 1], r - i + 1)
            while i - k - 1 >= 0 and i + k < n and s[i - k - 1] == s[i + k]:
                k += 1
            d_even[i] = k
            if i + d_even[i] - 1 > r:
                l = i - d_even[i]
                r = i + d_even[i] - 1
        return d_even

    def manacher_bounds(s):
        d_even = manacher_even(s)
        n = len(s)
        palindromic_pairs = [[] for _ in range(n)]
        for i in range(n):
            radius = d_even[i]
            for k in range(1, radius + 1):
                l = i - k
                r = i + k - 1
                palindromic_pairs[r].append(l)
        return palindromic_pairs



    input = sys.stdin.read().split()
    idx = 0
    t = int(input[idx])
    idx += 1
    for _ in range(t):
        n = int(input[idx])
        idx += 1
        s = input[idx]
        idx += 1

        pp = manacher_bounds(s)
        print(pp)
        dp = [0] * n
        count = sum(len(i) for i in pp)

        for r in range(n):
            for l in pp[r]:
                if l > 0:
                    dp[r] += dp[l - 1]
                dp[r] += 1
        print(dp)
        print(sum(dp))

main()
