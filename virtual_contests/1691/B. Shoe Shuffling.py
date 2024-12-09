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
    counts = {}
    for i, v in enumerate(a):
        if v in counts:
            counts[v].append(i)
        else:
            counts[v] = [i]
    for i in counts:
        if len(counts[i]) == 1:
            print(-1)
            break
    else:
        res = [0] * n
        for i in counts:
            curr = counts[i]
            for x in range(len(curr)):
                res[curr[x]] = curr[(x+1) % len(curr)] + 1
        print(ljoin(res))



#=============================================#

if __name__ == "__main__":
    for _ in range(ipt()): sol()
    #sol()
    pass



