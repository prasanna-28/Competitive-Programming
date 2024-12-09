
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
    n,s,t = ipt(), slist(), slist()
    pos = []

    tpos = []

    for i in range(1,n):
        if s[i] == '0' and s[i-1] == '1':
            pos.append(i)
        if s[i] == '1' and s[i-1] == '0':
            pos.append(i)
        if t[i] == '1' and t[i-1] == '0':
            tpos.append(i)
        if t[i] == '0' and t[i-1] == '1':
            tpos.append(i)
    pos.sort()
    tpos.sort()
    if len(pos) != len(tpos) or s[0] != t[0] or s[-1] != t[-1]:
        print(-1)
    else:
        tot = 0
        for i in range(len(pos)):
            tot += abs(pos[i] - tpos[i])
        print(tot)
'''
010011
010011

'''

#=============================================#

if __name__ == "__main__":
    for _ in range(ipt()): sol()
    #sol()
    pass



