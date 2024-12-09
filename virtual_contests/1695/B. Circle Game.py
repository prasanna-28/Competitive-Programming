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
    if n%2 == 1:
        print("Mike")
        return
    s = 0
    for i,v in enumerate(a):
        if v < a[s]:
            s = i

    if s%2 == 0:
        print("Joe")
    else:
        print("Mike")



#=============================================#



if __name__ == "__main__":
    for _ in range(ipt()): sol()
    #sol()
    pass



