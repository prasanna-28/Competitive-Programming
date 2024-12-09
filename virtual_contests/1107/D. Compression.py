
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
    pref = [[0]*(n+1) for i in range(n+1)]

    for i in range(n):
        matrix = bin(int(finp().strip(), 16))[2:].zfill(n)
        for j in range(0, n):
            pref[i+1][j+1] = int(matrix[j]) + pref[i+1][j]

    for i in range(1,n+1):
        for j in range(1, n+1):
            pref[i][j] += pref[i-1][j]


    matrix = 0

    factors = [n]

    for i in range(n//2, 1, -1):
        if n % i == 0:
            factors.append(i)

    for x in factors:
        prev = x**2
        possible = True
        for i in range(n//x):
            for j in range(n//x):
                row = (i+1)*x
                col = (j+1)*x
                s = pref[row][col] - pref[row][col-x] - pref[row-x][col] + pref[row-x][col-x]
                if s != 0 and s != prev:
                    possible = False
                    break
            else:
                continue
            break
        if possible:
            print(x)
            break
    else:
        print(1)
        return



#=============================================#

if __name__ == "__main__":
    #for _ in range(ipt()): sol()
    sol()
    pass



