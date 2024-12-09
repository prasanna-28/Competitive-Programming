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
    a,b,c = ilist(), ilist(), ilist()
    dsu = DSU(n)

    for i , (ai, bi, ci) in enumerate(zip(a, b, c)):
        dsu.union(ai-1, bi-1)
        if ai == bi:
            c[i] = ai

    k = set()
    o = set()
    for (ai, ci) in zip(a, c):
        k.add(dsu.get(ai-1) + 1)
        if ci != 0:
            o.add(dsu.get(ai-1) + 1)

    k = k - o
    print(pow(2, len(k), MOD))


#---------------------------------------------------
class DSU:
    def __init__(self, n):
        self.p = [i for i in range(n)]
        self.r = [1 for _ in range(n)]

    def get(self, a):
        if self.p[a] == a:
            return a
        self.p[a] = self.get(self.p[a])
        return self.p[a]

    def union(self, a, b):
        a = self.get(a)
        b = self.get(b)
        if a == b: return
        if self.r[a] >= self.r[b]:
            self.p[a] = self.p[b]
        else:
            self.p[b] = self.p[a]
        self.r[a] = self.r[a] + self.r[b]
        self.r[b] = self.r[a]

if __name__ == "__main__":
    for _ in range(ipt()): sol()
    #sol()
    pass
