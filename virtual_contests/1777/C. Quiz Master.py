import sys, math
from collections import deque, defaultdict, Counter

MOD       = 10**9 + 7
INF       = float('inf')
NINF      = float('-inf')
YES, NO   = "YES", "NO"
MT        = True

#---------------------------------------------------
def sol():
    n,m = ivars()
    a = ilist()
    adj = defaultdict(list)
    poss = [0] * (m+1)
    for i in a:
        factors = []
        for factor in range(1, math.isqrt(i) + 1):
            if factor > m:
                break
            if i % factor == 0:
                factors.append(factor)
                if i//factor != factor and i//factor <= m:
                    factors.append(i//factor)
        adj[i] = factors
        for f in factors:
            poss[f] += 1

    for i in poss[1:]:
        if i == 0:
            print(-1)
            return
    a.sort()
    mindiff = a[-1] - a[0]
    count = 0
    poss = [0] * (m+1)

    l = 0
    r = 0
    st = [0] * (m+1)

    while r <= n and l < n:
        while r < n and count != m:
            for factor in adj[a[r]]:
                if st[factor] == 0: count += 1
                st[factor] = st[factor] + 1
            r += 1
        if count == m:
            mindiff = min(mindiff, abs(a[l] - a[r-1]))
        else:
            break
        for factor in adj[a[l]]:
            st[factor] = st[factor] - 1
            if st[factor] == 0: count -= 1
        l += 1

    print(mindiff)


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

