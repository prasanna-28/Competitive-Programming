import sys, math
from collections import deque, defaultdict, Counter

MOD       = 10**9 + 7
FASTIO    = False
DEBUG     = False
INF       = float('inf')
NINF      = float('-inf')
YES, NO   = "YES", "NO"
MT        = True

#====================Solution====================
def sol():
    n, m1, m2 = ivars()
    adj1 = [[] for _ in range(n + 1)]
    adj2 = [[] for _ in range(n + 1)]
    edges1 = []
    edges2 = []
    for _ in range(m1):
        u, v = ivars()
        edges1.append((u, v))
    for _ in range(m2):
        u, v = ivars()
        edges2.append((u, v))
        adj2[u].append(v)
        adj2[v].append(u)
    seen = set()
    ccs = []
    for v in range(1, n+1):
        if str(v) in seen: continue
        seen.add(str(v))
        d = deque([v])
        curr = [v]
        while d:
            node = d.popleft()
            for child in adj2[node]:
                if str(child) not in seen:
                    seen.add(str(child))
                    curr.append(child)
                    d.append(child)
        ccs.append(curr)
    dsu = [0] * (n + 1)
    for i in range(len(ccs)):
        for j in ccs[i]:
            dsu[j] = i
    ops = 0
    new_F = []
    old = len(ccs)
    for u, v in edges1:
        if dsu[u] != dsu[v]:
            ops += 1
        else:
            new_F.append((u, v))
    for u, v in new_F:
        adj1[u].append(v)
        adj1[v].append(u)
    seen = set()
    ccs = []

    for v in range(1, n + 1):
        if str(v) not in seen:
            seen.add(str(v))
            d = deque([v])
            curr = [v]
            while d:
                node = d.popleft()
                for child in adj1[node]:
                    if str(child) not in seen:
                        seen.add(str(child))
                        curr.append(child)
                        d.append(child)
            ccs.append(curr)
    ops += (len(ccs) - old)
    print(ops)


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

