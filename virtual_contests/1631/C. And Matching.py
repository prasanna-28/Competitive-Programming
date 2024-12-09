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
    if k != n-1 and k != 0:
        print(n-1, k)
        print(0,k^(n-1))
        for i in range(n-2, n//2 - 1, -1):
            if i == k or i == k^(n-1): continue
            print(i, i^n-1)
    elif k == 0:
        for i in range(n-1, n//2 - 1, -1):

            print(i, i^(n-1))
    elif n != 4 and k == n-1:
        print(n-1, n-2)
        print(1, n-3)
        print(0, (n-3)^(n-1))
        for i in range(n-4, n//2 - 1, -1):
            if i != (n-3) ^ (n-1):
                print(i, i^(n-1))
    else:
        print(-1)




#=============================================#

if __name__ == "__main__":
    for _ in range(ipt()): sol()
    #sol()
    pass

'''
111

n-1 & n-2
1 & n-3
0 & inv(n-3)

111
110
101
100
011
010
001
000
'''

