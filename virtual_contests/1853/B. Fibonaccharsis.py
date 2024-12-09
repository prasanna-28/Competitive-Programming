
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
FIB = [0] * 35
FIB[0] = 0
FIB[1] = 1
for i in range(2,35):
    FIB[i] = FIB[i-1] + FIB[i-2]

def sol():
    n,k = ivars()
    k -= 1
    if k < len(FIB) and n == FIB[k]:
        print(1)
        return
    if k >= len(FIB) or k > n or n < FIB[k]:
        print(0)
        return

    count = 0

    for i in range(n):
        a = i
        if (n - FIB[k-1]*a) % FIB[k] == 0:
            if (n - FIB[k-1]*a)//FIB[k] >= a:
                count += 1

    print(count)






#=============================================#

if __name__ == "__main__":
    for _ in range(ipt()): sol()
    #sol()
    pass


'''
a b a+b a+2b 2a + 3b 3a + 5b 5a + 8b
0 1  2   3      4       5       6

0 1 1 2 3 5 8 ...
0 1 2 3 4 5 6

fib[k-1] a + fib[k]b = n
how many a and b fit this?

iterate on a, calculate b

b = (n - fib[k-1]*a)/fib[k]
'''
