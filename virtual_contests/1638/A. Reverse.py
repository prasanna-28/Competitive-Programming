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
    for i in range(n):
        if a[i] != i + 1:
            break
    else:
        print(ljoin(a))
        return
    find = i + 1
    for x in range(i, n):
        if a[x] == find:
            break
    first, mid, last = a[:i], a[i:x+1], a[x+1:]
    mid.reverse()
    print(ljoin(first + mid + last))






#=============================================#

if __name__ == "__main__":
    for _ in range(ipt()): sol()
    #sol()
    pass



