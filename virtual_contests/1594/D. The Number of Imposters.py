import   sys, math
from collections import defaultdict, deque
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
    n,m = ivars()
    adj = defaultdict(list)
    dummy = MOD
    for _ in range(m):
        q = input().split()
        u,v,t = int(q[0]), int(q[1]), q[2]
        if t == 'crewmate':
            adj[u].append(dummy)
            adj[dummy].extend([u,v])
            adj[v].append(dummy)
            dummy += 1
        else:
            adj[u].append(v)
            adj[v].append(u)
    visited = set()
    tot = 0
    colors = defaultdict(int)
    for i in range(1, n+1):
        if i in visited: continue
        colors[i] = 1
        q = deque([(i,1)])
        visited.add(i)
        c1 = 0
        c2 = 0
        while q:
            curr, color = q.popleft()
            if color == 1 and curr < 10**6:

                c1 += 1
            elif curr < 10**6:

                c2 += 1
            for x in adj[curr]:
                if x not in visited:
                    visited.add(x)
                    colors[x] = color ^ 1
                    q.append((x, color ^ 1))
                elif colors[x] == colors[curr]:
                    print(-1)
                    return

        tot += max(c1, c2)
    print(tot)


#---------------------------------------------------


if __name__ == "__main__":
    for _ in range(ipt()): sol()
    #sol()
    pass

'''
u v imposter -> u and v are opposite sides
u v crewmate -> u and v are on the same side
'''
