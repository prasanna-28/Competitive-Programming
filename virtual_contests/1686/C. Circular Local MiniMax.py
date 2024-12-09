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
    if n%2 == 1:
        print("NO")
        return
    a.sort()
    l = 0
    r = n // 2
    res = []
    for i in range(n):
        if i%2 == 0:
            res.append(a[l])
            l += 1
        else:
            res.append(a[r])
            r += 1
    rearrangement = res
    for i in range(n):
        left = rearrangement[(i - 1)%n]
        right = rearrangement[(i + 1)%n]
        mid = rearrangement[i]

        if (left >= mid and right <= mid or left <= mid and right >= mid):
            print("NO")
            break
    else:
        print("YES")
        print(ljoin(rearrangement))



#=============================================#

if __name__ == "__main__":
    for _ in range(ipt()): sol()
    #sol()
    pass

'''
1 1 2 2 2 | 3 3 4 4 5
1 3 1 3 2   4 2 4 2 5

0 0 0 1
1 1 1 1 2 3 4 5
1 2 1 3 1 4 1 5
'''
