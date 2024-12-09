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
    a,b,ab,ba = ivars()
    s = slist()
    n = len(s)
    s.reverse()
    while len(s) > 0:
        if len(s) >= 3:
            curr = s[-1] + s[-2] + s[-3]
            if curr == 'ABA':
                if a + ba > ab:
                    if ba < 1 or a < 1: break
                    ba -= 1
                    a -= 1
                    s.pop()
                    s.pop()
                    s.pop()
                else:
                    if ab < 1: break
                    ab -=1
                    s.pop()
                    s.pop()
                continue
            elif curr == 'BAB':
                if b + ab > ba:
                    if b < 1 or ab < 1: break
                    b -= 1
                    ab -=1
                    s.pop()
                    s.pop()
                    s.pop()
                else:
                    if ba < 1: break
                    ba -= 1
                    s.pop()
                    s.pop()
                continue
        if len(s) >= 2:
            curr = s[-1] + s[-2]
            if curr == 'AB':
                if ab > 0:
                    ab -= 1
                    s.pop()
                    s.pop()
                else:
                    if a < 1 or b < 1: break
                    a -= 1
                    b -= 1
                    s.pop()
                    s.pop()
                continue
            elif curr == 'BA':
                if ba > 0:
                    ba -= 1
                    s.pop()
                    s.pop()
                else:
                    if a < 1 or b < 1: break
                    a -= 1
                    b -= 1
                    s.pop()
                    s.pop()
                continue
        if len(s) >= 1:
            curr = s[-1]
            if curr == 'A':
                if a == 0: break
                a -= 1
                s.pop()
                continue
            elif curr == 'B':
                if b == 0: break
                b -= 1
                s.pop()
                continue
    else:
        print("YES")
        return
    print("NO")



# AB BA ABA BAB

#=============================================#

if __name__ == "__main__":
    for _ in range(ipt()): sol()
    #sol()
    pass


