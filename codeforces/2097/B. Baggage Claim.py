import sys, math
from collections import deque, defaultdict, Counter

MOD      = 10**9 + 7
FASTIO    = False
DEBUG     = False
INF       = float('inf')
NINF      = float('-inf')
YES, NO   = "YES", "NO"
MT        = True

#====================Solution====================
def sol():
    n, m, k = ivars()
    comps = defaultdict(list)
    cts = 0
    seen = {}
    x = 0
    pts = tuple(ivars())
    for i in range(1, k + 1):
        px, py = pts
        cx, cy = ivars()
        pts = (cx, cy)
        if abs(cx - px) + abs(cy - py) != 2:
            for _ in range(i + 1, k + 1):
                ivars()
            print(0)
            return
        if px == cx:
            cands = [(px, (py + cy)//2)]
        elif py == cy:
            cands = [((px + cx)//2, py)]
        else:
            cands = [(px, cy), (cx, py)]
        for l in cands:
            comps[i].append(l[0]*m + l[1])
            if l not in seen:
                cts += 1
                seen[l[0]*m + l[1]] = x
                x += 1
    dsu = DSU(cts)
    notgood = set()
    for i,v in comps.items():
        if len(v) <= 1:
            if seen[v[-1]] in notgood:
                print(0)
                return
            notgood.add(seen[v[-1]])
            continue
        curr = v[-1]
        for j in v[:-1]:
            dsu.join(seen[j], seen[curr])
    sizes = [0] * cts
    for i,v in comps.items():
        sizes[dsu.find(seen[v.pop()])] += 1
    comps = None
    seen = None
    res = 1
    newnotgood = set()
    for i in notgood:
        newnotgood.add(dsu.find(i))
    notgood = None
    visited = set()
    for i in range(cts):
        i = dsu.find(i)
        if i in visited:continue
        visited.add(i)
        cands = dsu.size[i]
        sz = sizes[i]
        if sz == cands:
            if i not in newnotgood:
                res *= 2
        elif cands == sz + 1:
            res *= cands
        else:
            print(0)
            return
        res %= MOD
    print(res)

#================================================

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.num_sets = n

    def find(self, a):
        acopy = a
        while a != self.parent[a]:
            a = self.parent[a]
        while acopy != a:
            self.parent[acopy], acopy = a, self.parent[acopy]
        return a

    def join(self, a, b):
        a, b = self.find(a), self.find(b)
        if a != b:
            if self.size[a] < self.size[b]:
                a, b = b, a

            self.num_sets -= 1
            self.parent[b] = a
            self.size[a] += self.size[b]

    def set_size(self, a):
        return self.size[self.find(a)]

    def __len__(self):
        return self.num_sets


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, a):
        acopy = a
        while a != self.parent[a]:
            a = self.parent[a]
        while acopy != a:
            self.parent[acopy], acopy = a, self.parent[acopy]
        return a

    def union(self, a, b):
        self.parent[self.find(b)] = self.find(a)

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


