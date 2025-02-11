import sys, math
from collections import deque, defaultdict, Counter
import heapq
MOD       = 10**9 + 7
FASTIO    = False
DEBUG     = False
INF       = float('inf')
NINF      = float('-inf')
YES, NO   = "YES", "NO"
MT        = True

#====================Solution====================
def sol():

    n, s1, s2 = ivars()

    m1 = ipt()
    g1 = [[] for _ in range(n+1)]
    for _ in range(m1):
        a, b = ivars()
        g1[a].append(b)
        g1[b].append(a)

    m2 = ipt()
    g2 = [[] for _ in range(n+1)]
    for _ in range(m2):
        c, d = ivars()
        g2[c].append(d)
        g2[d].append(c)

    good = [False]*(n+1)
    for v in range(1, n+1):
        if not g1[v] or not g2[v]:
            continue
        sset = set(g1[v])
        for x in g2[v]:
            if x in sset:
                good[v] = True
                break

    if s1 == s2 and good[s1]:
        print(0)
        return

    dist = [[INF]*(n+1) for _ in range(n+1)]
    dist[s1][s2] = 0
    heap = [(0, s1, s2)]
    ans = -1
    while heap:
        d, v1, v2 = heapq.heappop(heap)
        if d != dist[v1][v2]:
            continue
        if v1 == v2 and good[v1]:
            ans = d
            break
        for u in g1[v1]:
            nbrs2 = g2[v2]
            for w in nbrs2:
                nd = d + (u - w if u >= w else w - u)
                if nd < dist[u][w]:
                    dist[u][w] = nd
                    heapq.heappush(heap, (nd, u, w))
    if ans < 0:
        print(-1)
    else:
        print(ans)



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

