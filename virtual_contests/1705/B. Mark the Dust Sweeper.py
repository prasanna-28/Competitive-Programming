
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
    a = ilist()
    l = 0
    while l < n and a[l] == 0: l += 1
    ctr = 0
    while l < n-1:
        if a[l] == 0: ctr += 1
        l += 1
    print(sum(a[:n-1]) + ctr)





#=============================================#

if __name__ == "__main__":
    for _ in range(ipt()): sol()
    #sol()
    pass



