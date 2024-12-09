
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
    T = set()
    q = []
    for i in range(n):
        k = set(ilist()[1:])
        q.append(k)
        T |= k
    tot = 0
    for x in T:
        curr = set()
        for i in q:
            if x not in i:
                curr |= i
        tot = max(tot, len(curr))

    print(tot)




#=============================================#

if __name__ == "__main__":
    for _ in range(ipt()): sol()
    #sol()
    pass



