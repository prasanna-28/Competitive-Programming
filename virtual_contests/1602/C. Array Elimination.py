import   sys, math
MOD    = 10**9 + 7
INF    = float('inf')
NINF   = float('-inf')
YES,NO = "Yes", "No"
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

#---------------------------------------------------
def sol():
    n = ipt()
    a = ilist()
    if all([i == 0 for i in a]):
        print(ljoin(list(range(1, n+1))))
        return
    cts = []
    for bit in range(31):
        ct = 0
        for i in a:
            if not i & (1<<bit):
                ct += 1
        cts.append(ct)
    x = math.gcd(*cts)
    res = []
    for i in range(1, x+1):
        if all([ct % i == 0 for ct in cts]):
            res.append(i)
    print(ljoin(res))

#---------------------------------------------------
if __name__ == "__main__":
    for _ in range(ipt()): sol()
    #sol()
    pass
