import   sys, math
from itertools import accumulate
MOD    = 10**9 + 7
INF    = float('inf')
NINF   = float('-inf')
YES,NO = "YES", "NO"
DEBUG  = 0
finp   = sys.stdin.readline
njoin  = lambda x: '\n'.join(map(str, x))
ljoin  = lambda x: ' '.join(map(str, x))
sjoin  = lambda x: '\n'.join(x)
ilist  = lambda: list(map(int, finp().split()))
slist  = lambda: list(input())
slists = lambda: input().split()
ivars  = lambda: map(int, finp().split())
ipt    = lambda: int(finp())
debug  = lambda **kwargs: (print("Dbg:"), print("\n".join([f"{key} = {value}" for key, value in kwargs.items()]))) if DEBUG else None
out = []
#---------------------------------------------------
def sol():
    n,k = ivars()
    a = ilist()
    a.sort(reverse = k <= 0)
    a = [0] + a
    found = False
    for i in accumulate(a):
        if i >= k:
            found = True
        if found and i < k:
            print("No")
            return
    print("Yes")
    print(ljoin(a[1:]))


#---------------------------------------------------
if __name__ == "__main__":
    #for _ in range(ipt()): sol()
    sol()
    pass
