import   sys, math
from bisect import bisect_left
MOD    = 10**9 + 7
INF    = float('inf')
NINF   = float('-inf')
YES,NO = "Yes", "No"
DEBUG  = 0
finp   = sys.stdin.readline
njoin  = lambda x: '\n'.join(map(str, x))
ljoin  = lambda x: ' '.join(map(str, x))
sjoin  = lambda x: '\n'.join(x)
ilist  = lambda: list(map(int, finp().split()))
slist  = lambda: list(input())
slists = lambda: input().split()
ivars  = lambda: map(int, finp().split())
ipt    = lambda: int(finp())
debug  = lambda **kwargs: (print("Dbg:"), print("\n".join([f"{key} = {value}" for key, value in kwargs.items()]))) if DEBUG else None

#---------------------------------------------------

def sol():
    n,k = ivars()
    a = ilist()
    counts = {}
    def cost(i, start):
        indexes = counts[a[i]]
        id = bisect_left(indexes, start)
        right = bisect_left(indexes, i)
        if id == right or len(indexes) == 1:
            return 0
        else:
            return i - indexes[right - 1]

    for i,v in enumerate(a):
        if v in counts:
            counts[v].append(i)
        else:
            counts[v] = [i]
    dp = [[(INF, INF)] * k for _ in range(n)]
    for i in range(k):
        dp[0][i] = (0,0)
    for i in range(1, n):
        dp[i][0] = (dp[i-1][0][0] + cost(i, 0), 0)
    for i in range(1, n):
        for j in range(1, k):
            dp[i][j] = min(dp[i][j], (dp[i-1][j][0] + cost(i, dp[i-1][j][1]), dp[i-1][j][1]), (dp[i-1][j-1][0], i), key = lambda x: (x[0], -x[1]))
    for i in dp:
        print(i)

    print(dp[n-1][k-1][0])


#---------------------------------------------------
if __name__ == "__main__":
    #for _ in range(ipt()): sol()
    sol()
    pass

'''
dp[i][k] -> cost up to i using k divisions
store (cost, start) tuples
transitions:
    dp[i][k] = min((dp[i-1][k][0] + cost(i, dp[i-1][1]), dp[i-1][1]), (dp[i-1][k-1][0], i), key = lambda x: x[0])
how to calculate cost?

def cost(i, start):
    indexes = counts[a[i]]
    idx = bisect_left(a, start)
    if idx < len(indexes):
        return i - idx
    return 0
what to start with?
first row is all costs
first col is all (0,0)

'''
