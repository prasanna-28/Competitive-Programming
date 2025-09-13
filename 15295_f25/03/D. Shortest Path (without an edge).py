import sys, math
from collections import deque, defaultdict, Counter
import heapq
MOD       = 10**9 + 7
FASTIO    = False
DEBUG     = False
INF       = float('inf')
NINF      = float('-inf')
YES, NO   = "YES", "NO"
MT        = not True

#====================Solution====================
def sol():
    n, m = ivars()
    adj = [[] for _ in range(n + 1)]
    adjrev = [[] for _ in range(n + 1)]
    edges = []
    for _ in range(m):
        u, v = ivars()
        adj[u].append(v)
        adjrev[v].append(u)
        edges.append((u, v))

    q = deque([1])
    dist1 = [-1] * (n + 1)
    dist1[1] = 0
    while q:
        node = q.popleft()
        for i in adj[node]:
            if dist1[i] == -1:
                dist1[i] = dist1[node] + 1
                q.append(i)

    dist2 = [-1] * (n + 1)
    dist2[n] = 0
    q = deque([n])
    while q:
        node = q.popleft()
        for child in adjrev[node]:
            if dist2[child] == -1:
                dist2[child] = dist2[node] + 1
                q.append(child)

    D = dist1[n]
    if D == -1:
        print("\n".join(["-1"] * m))
        return

    dag = [[] for _ in range(n + 1)]
    rdag = [[] for _ in range(n + 1)]
    ond = [False] * m
    for i, (u, v) in enumerate(edges):
        if dist1[u] != -1 and dist2[v] != -1 and dist1[u] + 1 + dist2[v] == D and dist1[v] == dist1[u] + 1:
            ond[i] = True
            dag[u].append(v)
            rdag[v].append(u)

    layers = [[] for _ in range(D + 1)]
    for v in range(1, n + 1):
        if dist1[v] != -1 and dist2[v] != -1 and dist1[v] + dist2[v] == D:
            layers[dist1[v]].append(v)

    ways1 = [0] * (n + 1)
    ways1[1] = 1
    for d in range(D):
        for u in layers[d]:
            w = ways1[u]
            if w:
                for v in dag[u]:
                    ways1[v] += w

    waysN = [0] * (n + 1)
    waysN[n] = 1
    for d in range(D, 0, -1):
        for v in layers[d]:
            w = waysN[v]
            if w:
                for u in rdag[v]:
                    waysN[u] += w

    S = ways1[n]

    def bfs(a, b):
        dq = deque([1])
        dist = [-1] * (n + 1)
        dist[1] = 0
        while dq:
            u = dq.popleft()
            for v in adj[u]:
                if u == a and v == b:
                    continue
                if dist[v] == -1:
                    dist[v] = dist[u] + 1
                    dq.append(v)
        return dist[n]

    ans = [0] * m
    for i, (u, v) in enumerate(edges):
        if not ond[i]:
            ans[i] = D
        else:
            if ways1[u] * waysN[v] == S:
                ans[i] = bfs(u, v)
            else:
                ans[i] = D

    for i in ans:
        print(i)





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

