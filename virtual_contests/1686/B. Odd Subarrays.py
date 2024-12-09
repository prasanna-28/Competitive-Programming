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
    i = 1
    subs = 0
    while i < n:
        if a[i] < a[i-1]:
            subs += 1
            i += 2
            continue
        i += 1
    print(subs)




#=============================================#

if __name__ == "__main__":
    for _ in range(ipt()): sol()
    #sol()
    pass



