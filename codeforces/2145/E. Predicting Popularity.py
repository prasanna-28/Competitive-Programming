import sys, math
from collections import deque, defaultdict, Counter

MOD       = 10**9 + 7
FASTIO    = False
DEBUG     = False
INF       = float('inf')
NINF      = float('-inf')
YES, NO   = "YES", "NO"
MT        = False

#====================Solution====================

def sol():
    ac, dr = ivars()
    n = ipt()
    a = ilist()
    d = ilist()
    m = ipt()

    s = [min(n, max(0, a[i] - ac) + max(0, d[i] - dr)) for i in range(n)]
    freq = [0]*(n+1)
    for v in s:
        freq[v] += 1

    size = 1
    while size < n + 1:
        size <<= 1
    segsum = [0]*(2*size)
    segmin = [0]*(2*size)

    for i in range(n+1):
        segsum[size + i] = freq[i] - 1
        segmin[size + i] = freq[i] - 1
    for i in range(size - 1, 0, -1):
        segsum[i] = segsum[i << 1] + segsum[i << 1 | 1]
        segmin[i] = min(segmin[i << 1], segsum[i << 1] + segmin[i << 1 | 1])

    for t in range(m):
        k, ai, di = ivars()
        k -= 1
        i = size + s[k]
        segsum[i] -= 1
        segmin[i] -= 1
        i >>= 1
        while i:
            segsum[i] = segsum[i << 1] + segsum[i << 1 | 1]
            segmin[i] = min(segmin[i << 1], segsum[i << 1] + segmin[i << 1 | 1])
            i >>= 1

        a[k], d[k] = ai, di
        r = max(0, ai - ac) + max(0, di - dr)
        s[k] = min(n, r)

        i = size + s[k]
        segsum[i] += 1
        segmin[i] += 1
        i >>= 1
        while i:
            segsum[i] = segsum[i << 1] + segsum[i << 1 | 1]
            segmin[i] = min(segmin[i << 1], segsum[i << 1] + segmin[i << 1 | 1])
            i >>= 1

        if segmin[1] >= 0:
            print(n + 1)
        else:
            acc = 0
            i = 1
            while i < size:
                L = i << 1
                if segmin[L] + acc < 0:
                    i = L
                else:
                    acc += segsum[L]
                    i = L | 1
            pos = i - size
            print(pos)

#================================================
class FenwickTree:
    def __init__(self, x):
        """transform list into BIT"""
        self.bit = x
        for i in range(len(x)):
            j = i | (i + 1)
            if j < len(x):
                x[j] += x[i]

    def update(self, idx, x):
        """updates bit[idx] += x"""
        while idx < len(self.bit):
            self.bit[idx] += x
            idx |= idx + 1

    def query(self, end):
        """calc sum(bit[:end])"""
        x = 0
        while end:
            x += self.bit[end - 1]
            end &= end - 1
        return x


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

