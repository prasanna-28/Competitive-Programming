
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
    n,c,q = ivars()
    s = slist()
    pref = [len(s)]
    ops = [(0, len(s))]
    for _ in range(c):
        l,r = ivars() # one indexed, inclusive
        ops.append((l-1,r))
        pref.append(pref[-1] + r - l + 1)


    for _ in range(q):
        k = ipt()-1
        while k >= len(s):
            x = binsearch(pref, k)
            k += ops[x][0]
            k -= pref[x-1]
        print(s[k])

'''
markmarkmarrkmark
'''
#=============================================#
def binsearch(arr, target):
    left = 0
    right = len(arr) - 1
    result = -1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] > target:
            result = mid
            right = mid - 1
        else:
            left = mid + 1

    return result

if __name__ == "__main__":
    for _ in range(ipt()): sol()
    #sol()
    pass



