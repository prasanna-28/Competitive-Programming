import sys, math
from collections import deque, defaultdict, Counter
from heapq import heappush as hpush, heappop as hpop, heapify
MOD       = 10**9 + 7
FASTIO    = False
DEBUG     = False
INF       = float('inf')
NINF      = float('-inf')
YES, NO   = "YES", "NO"
MT        = True
#====================Solution====================
def sol():
    n = ipt()
    g = [[] for _ in range(n+1)]
    for _ in range(n-1):
        u,v = ivars()
        g[u].append(v)
        g[v].append(u)
    alive = [True]*(n+1)
    dist = [-1]*(n+1)
    parent = [-1]*(n+1)
    def dia(s):
        v1 = [s]
        dq = deque([s])
        dist[s] = 0
        f = s
        while dq:
            u = dq.popleft()
            if dist[u] > dist[f] or (dist[u] == dist[f] and u > f): f = u
            for w in g[u]:
                if alive[w] and dist[w]==-1:
                    dist[w] = dist[u]+1
                    v1.append(w)
                    dq.append(w)
        for x in v1: dist[x] = -1
        v2 = [f]
        dq = deque([f])
        dist[f] = 0
        parent[f] = -1
        f2 = f
        while dq:
            u = dq.popleft()
            if dist[u]>dist[f2] or (dist[u]==dist[f2] and u>f2): f2 = u
            for w in g[u]:
                if alive[w] and dist[w]==-1:
                    dist[w] = dist[u]+1
                    parent[w] = u
                    v2.append(w)
                    dq.append(w)
        path = []
        u = f2
        while u!=-1:
            path.append(u)
            u = parent[u]
        for x in v2:
            dist[x] = -1
            parent[x] = -1
        u1, v1m = max(path[0], path[-1]), min(path[0], path[-1])
        return len(path), u1, v1m, path

    h = []
    cnt = 0
    d, u, v, p = dia(1)
    cnt += 1
    h.append((-d, -u, -v, cnt, p))
    heapify(h)
    ans = []
    while h:
        dneg, uneg, vneg, _, p = hpop(h)
        d, u, v = -dneg, -uneg, -vneg
        ans.extend([d, u, v])
        for x in p:
            alive[x] = False
        for x in p:
            for y in g[x]:
                if alive[y]:
                    d2, u2, v2, p2 = dia(y)
                    cnt += 1
                    hpush(h, (-d2, -u2, -v2, cnt, p2))
    print(ljoin(ans))


#================================================

def main():
    for _ in range(ipt() if MT else 1):
        sol()


def debug(*args):
    if DEBUG:
        for arg in args:
            print(arg)

def ASSERT(cond):
    if DEBUG:
        assert(cond)


if FASTIO:
    import os
    from io import BytesIO, IOBase

    _str = str
    str = lambda x=b"": x if type(x) is bytes else _str(x).encode()

    BUFSIZE = 8192


    class FastIO(IOBase):
        newlines = 0

        def __init__(self, file):
            self._file = file
            self._fd = file.fileno()
            self.buffer = BytesIO()
            self.writable = "x" in file.mode or "r" not in file.mode
            self.write = self.buffer.write if self.writable else None

        def read(self):
            while True:
                b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
                if not b:
                    break
                ptr = self.buffer.tell()
                self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
            self.newlines = 0
            return self.buffer.read()

        def readline(self):
            while self.newlines == 0:
                b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
                self.newlines = b.count(b"\n") + (not b)
                ptr = self.buffer.tell()
                self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
            self.newlines -= 1
            return self.buffer.readline()

        def flush(self):
            if self.writable:
                os.write(self._fd, self.buffer.getvalue())
                self.buffer.truncate(0), self.buffer.seek(0)


    class IOWrapper(IOBase):
        def __init__(self, file):
            self.buffer = FastIO(file)
            self.flush = self.buffer.flush
            self.writable = self.buffer.writable
            self.write = lambda s: self.buffer.write(s.encode("ascii"))
            self.read = lambda: self.buffer.read().decode("ascii")
            self.readline = lambda: self.buffer.readline().decode("ascii")


    sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
    input = lambda: sys.stdin.readline().rstrip("\r\n")

if __name__ == "__main__":
    finp        = sys.stdin.readline
    njoin       = lambda x: '\n'.join(map(str, x))
    ljoin       = lambda x: ' '.join(map(str, x))
    sjoin       = lambda x: '\n'.join(x)
    ilist       = lambda: list(map(int, finp().split()))
    slist       = lambda: list(input())
    slists      = lambda: input().split()
    ivars       = lambda: map(int, finp().split())
    ipt         = lambda: int(finp())
    main()

