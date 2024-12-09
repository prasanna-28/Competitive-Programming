
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

    score = 0

    i = 0

    # find first positive
    while i < n and a[i] < 0:
        i += 1

    if i >= n:
        # all elements negative
        print(0)
        return

    # can just add all elements, no special case
    if i % 2 == 0:
        for x in range(i, n):
            if a[x] > 0:
                score += a[x]
    else:
        if i > 1:
            adder = a[i]
        else:
            adder = max(a[0] + a[1], 0)

        # add all positive elements after i
        for x in range(i+1, n):
            if a[x] > 0:
                score += a[x]

        # add the adder
        score += adder

    print(score)


#=============================================#

if __name__ == "__main__":
    for _ in range(ipt()): sol()
    #sol()
    pass



