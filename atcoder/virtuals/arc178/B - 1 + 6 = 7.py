import   sys, math
finp   = sys.stdin.readline
MOD    = 998244353
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
    a,b,c = ivars()
    a,b = max(a,b), min(a,b)
    if c == a:
        k = (8 * pow(10, b-1, MOD)) % MOD
        inv_2 = pow(2, -1, MOD)
        k = (k * (k+1)) % MOD
        k = (k * inv_2) % MOD
        print(k)

    elif c == a + 1:
        num = (9 * pow(10, b - 1)) % MOD
        inv_2 = pow(2, -1, MOD)
        res = (num * (num + 1)) % MOD
        print((res * inv_2) % MOD)
    else:
        print(0)

#=============================================#

'''
each n has 9 - n
8 1
7 1 2
6 -> 3
5 -> 4
...
1 -> 8

each n has 90 - n
89 10 -> 1
88 10 11 -> 2
87 -> 3
...
10 -> 90

100

899 -> 1
898 -> 2

100 -> 800

fix first number, find second

900 * 901 // 2



n digits ->
9 * 10 ** (n-1) - (k) for all k from 10 ** (n-1) ...
sum of all this is double digits

let digits be n

9 * (10 ** (n-1)) = k
1 * (10 ** (n-1)) = p

num = k(k+1)//2 - (o)(o-1)//2


89999...999
10000...000

999999999 -> all numbers with b digits works
999999998 -> above minus 1
999999997 -> continue

goes on for all numbers with b digits
how many numbers have b digits?
9 ** 10

9



'''

def binexp(a, b, P = MOD):
    r = 1
    while b>0:
        if b%2 == 1:
            r = (r * a) % P
        a = (a * a) % P
        b //= 2

    return r % P


def invmod(a, b, P = MOD):
    return a * binexp(b, P-2, P) % P

if __name__ == "__main__":
    for _ in range(ipt()): sol()
    #sol()
    pass



