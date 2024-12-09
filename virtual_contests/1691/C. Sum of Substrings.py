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
    s = slist()
    oc = 0
    start = 0
    end = n - 1
    for i in s:
        if i == '1':
            oc += 1
    if oc == 0:
        print(0)
        return
    while s[start] != '1': start += 1
    while s[end] != '1': end -= 1
    distend = n - end - 1
    diststart = start
    if oc == 1:
        if distend <= k:
            s[end] = '0'
            s[-1] = '1'
        elif diststart <= k:
            s[start] = '0'
            s[0] = '1'
    else:
        if distend <= k:
            s[end] = '0'
            s[-1] = '1'
            k -= distend
        if diststart <= k:
            s[start] = '0'
            s[0] = '1'
    tot = 0
    for i in range(1, n):
        curr = s[i-1] + s[i]
        tot += int(curr)
    print(tot)




#=============================================#

if __name__ == "__main__":
    for _ in range(ipt()): sol()
    #sol()
    pass


'''
100001101
10 + 1 + 11 + 10 + 1
10 + 1 + 10 + 1 + 11
10 + 1 + 11 + 11
'''
