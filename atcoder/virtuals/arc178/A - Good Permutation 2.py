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
    a = ilist()
    a = set(a)
    if 1 in a or n in a:
        print(-1)
        return
    p = []
    curr = None
    for i in range(1, n+1):
        if i in a:
            if curr == None:
                curr = i
            else:
                p.append(i)
        else:
            p.append(i)
            if curr != None:
                p.append(curr)
                curr = None
    print(ljoin(p))


#=============================================#
'''
2 5 6
1 2 3 4 5 6 7
1 3 2 4 7 5 6
'''
if __name__ == "__main__":
    #for _ in range(ipt()): sol()
    sol()
    pass



