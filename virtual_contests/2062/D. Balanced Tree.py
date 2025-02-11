import sys, math
from collections import deque, defaultdict, Counter

MOD       = 10**9 + 7
FASTIO    = True
DEBUG     = False
INF       = float('inf')
NINF      = float('-inf')
YES, NO   = "YES", "NO"
MT        = True

#====================Solution====================
def sol():
    n = ipt()
    lrs = []
    for _ in range(n):
        lrs.append(tuple(ivars()))
    adj = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = ivars()
        u -= 1
        v -= 1
        adj[u].append(v)
        adj[v].append(u)
    root = 0
    for i in range(1, n):
        if lrs[i][0] >= lrs[root][0]:
            root = i

    stack = [root]
    seen = set([root])
    p = [-1] * n
    while stack:
        node = stack.pop()
        for child in adj[node]:
            if child in seen: continue
            p[child] = node
            stack.append(child)
            seen.add(child)

    vals = [-1] * n
    vals[root] = lrs[root][0]
    d = [(root, -1)]
    while d:
        node, val = d.pop()
        if val == -1:
            d.append((node, 1))
            for child in adj[node]:
                if child != p[node]:
                    d.append((child, -1))
        else:
            children = []
            for child in adj[node]:
                if child != p[node]:
                    children.append(vals[child])
            if len(children) == 0:
                vals[node] = lrs[node][0]
            else:
                mx = max(children)
                if mx <= lrs[node][0]:
                    vals[node] = lrs[node][0]
                elif mx >= lrs[node][1]:
                    vals[node] = lrs[node][1]
                else:
                    vals[node] = mx

    d = deque([root])
    mxval = vals[root]
    while d:
        node = d.popleft()
        for child in adj[node]:
            if child != p[node]:
                if vals[child] >= vals[node]:
                    mxval += vals[child] - vals[node]
                d.append(child)

    print(mxval)



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

