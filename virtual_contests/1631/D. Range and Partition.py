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
    counts = {}
    for i in a:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1
    p = []
    s = 0
    for i in counts:
        p.append((i, counts[i]))
        s += counts[i]
    p.sort(key = lambda x: x[0])
    xy = [0, float('inf')]
    l = 0
    r = 0
    curr = 0
    while r < len(p):
        while r < len(p) and 2 * (curr + p[r][1]) - s < k:
            curr += p[r][1]
            r += 1
        if r >= len(p):
            break
        if p[r][0] - p[l][0] < xy[1] - xy[0]:
            xy = [p[l][0], p[r][0]]
        curr -= p[l][1]
        l += 1
    b = [0] * n
    x,y = xy
    for i in range(n):
        if x <= a[i] <= y:
            b[i] = 1
        else:
            b[i] = -1
    for i in range(1, n):
        b[i] = b[i-1] + b[i]
    print(x,y)
    seen = 0
    oc = 1
    l = 1
    for i in range(len(b)):
        if seen == k - 1:
            print(l, n)
            break
        if b[i] == oc:
            print(l, i + 1)
            oc += 1
            l = i + 2
            seen += 1




#=============================================#

if __name__ == "__main__":
    for _ in range(ipt()): sol()
    #sol()
    pass



