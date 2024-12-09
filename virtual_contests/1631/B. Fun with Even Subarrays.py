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
    same = a[-1]
    start = n - 1
    ops = 0
    length = 0
    while start >= 0:
        while start >= 0 and a[start] == same:
            start -= 1
            length += 1
        if start < 0: break
        ops += 1
        for _ in range(length):
            if start >= 0:
                a[start] = same
                start -= 1
        length *= 2
    print(ops)





#=============================================#

if __name__ == "__main__":
    for _ in range(ipt()): sol()
    #sol()
    pass



