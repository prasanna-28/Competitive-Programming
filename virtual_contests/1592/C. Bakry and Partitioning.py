import   sys, math
from types import GeneratorType
sys.setrecursionlimit(125000)
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

#-----------------------------------------------
def sol():
    n,k = ivars()
    a = ilist()
    adj = {}
    for _ in range(n-1):
        u,v = ivars()
        if (u, a[u-1]) in adj:
            adj[(u, a[u-1])].add((v, a[v-1]))
        else:
            adj[(u, a[u-1])] = {(v, a[v-1])}
        if (v, a[v-1]) in adj:
            adj[(v, a[v-1])].add((u, a[u-1]))
        else:
            adj[(v, a[v-1])] = {(u, a[u-1])}

    xor = 0
    for i in a: xor ^= i
    if xor == 0:
        # removing any edge works
        print(YES)
        return
    # exactly 2 edges must be removed
    # xor total of each component must be equal to xor
    x = [0] * (n+1)
    seen = set()
    seen.add((1, a[0]))
    def dfs(vi):
        v,value = vi

        for i in adj[vi]:
            if i in seen: continue
            seen.add(i)
            b = dfs(i)
            if b: return 1
            x[v] ^= x[i[0]]
        else:
            x[v] ^= value
            if x[v] == xor:
                return 1
            else:
                return 0

    e1 = dfs((1, a[0]))
    if not e1:
        print(NO)
        return
    for e1, i in enumerate(x):
        if i == xor and e1 != 1:
            e1 = (e1, a[e1 - 1])
            for v in adj[e1]:
                if e1 in adj[v]: adj[v].remove(e1)
            break
    else:
        print(NO)
        return
    x = [0] * (n+1)
    seen = set()
    seen.add((1, a[0]))
    e2 = dfs((1, a[0]))
    if e2:
        print(YES)
    else:
        print(NO)



def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to
    return wrappedfunc
#-----------------------------------------------
if __name__ == "__main__":
    for _ in range(ipt()): sol()
    #sol()
    pass







