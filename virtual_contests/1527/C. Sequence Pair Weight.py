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
    idx = {}
    for i,v in enumerate(a):
        if v in idx:
            idx[v].append(i)
        else:
            idx[v] = [i]
    tot = 0
    for v in idx:
        if len(idx[v]) >= 2:
            sum = 0
            for i in idx[v]:
                tot += (n - i) * sum
                sum += i + 1

    print(tot)


#---------------------------------------------------
if __name__ == "__main__":
    for _ in range(ipt()): sol()
    #sol()
    pass


'''
a1 a2 a3

(n - a3) * (a2 + 1) + (n - a3) * (a1 + 1) + (n - a2) * (a1 + 1)
(n - a3) * (a2 + a1 + 1 + 1) + (n - a2) * (a1 + 1)

a1 a2 a3 a4




'''
