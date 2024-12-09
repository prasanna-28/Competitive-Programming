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
    n,m = ivars()
    grid = []
    maximum = NINF
    coords = (0,0)
    for i in range(n):
        a = ilist()
        for j in range(m):
            if a[j] > maximum:
                maximum = a[j]
                coords = (i,j)
    i,j = coords[0], coords[1]
    x = max(i+1, n-i)
    y = max(j+1, m-j)
    print(x*y)



#=============================================#

if __name__ == "__main__":
    for _ in range(ipt()): sol()
    #sol()
    pass



