
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
    n,k = ivars()
    a = ilist()
    s = slist()
    c = {}

    i = 0
    tot = 0
    while i < len(s):
        counters = []
        start = s[i]
        while i < len(s) and s[i] == start:
            counters.append(a[i])
            i += 1
        counters.sort(reverse = True)
        for x in range(min(k, len(counters))):
            tot += counters[x]

    print(tot)


#=============================================#

if __name__ == "__main__":
    #for _ in range(ipt()): sol()
    sol()
    pass



