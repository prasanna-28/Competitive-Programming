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
    seen = set()
    start = {}
    end = {}
    for i in range(n):
        if a[i] not in start:
            start[a[i]] = i

    for i in range(n-1, -1, -1):
        if a[i] not in end:
            end[a[i]] = i


    sweep = []
    for i in start:
        if i in end:
            sweep.append((start[i], end[i]))

    sweep.sort(key = lambda x: x[0])
    newsweep = []
    seen = set()
    i = 0
    while i < len(sweep):
        if i < len(sweep) - 1 and sweep[i+1][1] <= sweep[i][1]:
            newsweep.append(sweep[i])
            seen.add(sweep[i][0])
            seen.add(sweep[i][1])
            i += 2
            continue
        seen.add(sweep[i][0])
        seen.add(sweep[i][1])
        newsweep.append(sweep[i])
        i += 1
    sweep = newsweep
    tot = 0
    i = 0
    while i < len(sweep)-1:
        if sweep[i+1][0] < sweep[i][1]:
            tot += max(sweep[i+1][0] - sweep[i][0] - 1, 0)
            i += 1
            continue
        tot += max(sweep[i][1] - sweep[i][0] -1, 0)
        i += 1
    tot += max(sweep[-1][1] - sweep[-1][0] - 1, 0)
    print(tot)


#=============================================#

if __name__ == "__main__":
    #for _ in range(ipt()): sol()
    sol()
    pass



