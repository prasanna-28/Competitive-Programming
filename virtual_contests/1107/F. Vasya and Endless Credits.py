
import   sys, math
finp   = sys.stdin.readline
MOD    = 10**9 + 7
njoin  = lambda x: '\n'.join(map(str, x))
ljoin  = lambda x: ' '.join(map(str, x))
sjoin  = lambda x: '\n'.join(x)
initl  = lambda x,y: [y]*x
INF    = float('inf')
NINF   = float('-inf')
ilist  = lambda: list(map(int, finp().split()))
slist  = lambda: list(input())
slists = lambda: input().split()
ivars  = lambda: map(int, finp().split())
ipt    = lambda: int(finp())
out    = []
#=============================================#
def sol():
    n = ipt()
    a = []
    for i in range(n):
        ai,bi,ki = ivars()
        a.append((ai, bi, ki))

    # bank gives ai and pay back bi for next ki
    # maximize some sum(ai) - sum(bi)*months -> minimize Bi or months?

    a.sort(key = lambda x: x[1], reverse = True)

    dp = [0] * (n+1)



    for i in a:
        A,B,K = i[0],i[1],i[2]
        ut = B*K
        for j in range(n, 0, -1):
            sf = B*(j-1)
            dp[j] = max(dp[j], dp[j-1] + A - sf)
            dp[j-1] = max(dp[j-1], dp[j-1] + A - ut)



    print(max(dp))



'''
    dp[i] = max(dp[i], f(i, A, B))
    dp[i-1] = max(dp[i-1], g(i, A, B, k))
    f(x) use first i months
    g(x) use all k months
'''

#=============================================#

if __name__ == "__main__":
    #for _ in range(ipt()): sol()
    sol()
    pass



