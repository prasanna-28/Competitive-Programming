import sys, math
from collections import deque, defaultdict, Counter

MOD       = 10**9 + 7
FASTIO    = False
DEBUG     = False
inf       = float('inf')
NINF      = float('-inf')
YES, NO   = "YES", "NO"
MT        = True

#====================Solution====================
def sol():
    n = ipt()
    h = [ilist() for _ in range(n)]
    a = ilist()
    b = ilist()
    R = [[[False, False], [False, False]] for _ in range(n - 1)]
    C = [[[False, False], [False, False]] for _ in range(n - 1)]

    for i in range(n - 1):
        for j in range(n):
            for u in (0, 1):
                x = h[i][j] + u
                for v in (0, 1):
                    if x == h[i + 1][j] + v:
                        R[i][u][v] = True

    for j in range(n - 1):
        for i in range(n):
            for u in (0, 1):
                x = h[i][j] + u
                for v in (0, 1):
                    if x == h[i][j + 1] + v:
                        C[j][u][v] = True

    x0, x1 = 0, a[0]
    for i in range(1, n):
        y0 = min(x0 if not R[i - 1][0][0] else inf,
                 x1 if not R[i - 1][1][0] else inf)
        y1 = min((x0 if not R[i - 1][0][1] else inf) + a[i],
                 (x1 if not R[i - 1][1][1] else inf) + a[i])
        x0, x1 = y0, y1
    u = min(x0, x1)

    x0, x1 = 0, b[0]
    for j in range(1, n):
        y0 = min(x0 if not C[j - 1][0][0] else inf,
                 x1 if not C[j - 1][1][0] else inf)
        y1 = min((x0 if not C[j - 1][0][1] else inf) + b[j],
                 (x1 if not C[j - 1][1][1] else inf) + b[j])
        x0, x1 = y0, y1
    v = min(x0, x1)

    print(u + v if u < inf and v < inf else -1)

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

