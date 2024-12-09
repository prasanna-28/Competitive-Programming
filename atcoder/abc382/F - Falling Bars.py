import sys, math
from collections import deque, defaultdict, Counter

MOD       = 10**9 + 7
FASTIO    = True
DEBUG     = False
INF       = float('inf')
NINF      = float('-inf')
YES, NO   = "YES", "NO"
MT        = False

#====================Solution====================
def sol():
    h, w, n = ivars()
    k = []
    for i in range(n):
        r, c, l = ivars()
        k.append((r, c, l, i))
    k.sort(reverse = True)
    seg = LazySegmentTree([0] * (w + 5))
    res = [0] * n
    for r, c, l, i in k:
        pos = seg.query(c, c + l)
        res[i] = h - pos
        seg.assign(c, c + l, pos + 1)
    for i in res:
        print(i)

#================================================

class LazySegmentTree:
    def __init__(self, data, default=0, func=max):
        """Initialize the lazy segment tree with data."""
        self._default = default
        self._func = func

        self._len = len(data)
        self._size = _size = 1 << (self._len - 1).bit_length()
        self._lazy = [None] * (2 * _size)

        self.data = [default] * (2 * _size)
        self.data[_size:_size + self._len] = data
        for i in reversed(range(1, _size)):
            self.data[i] = func(self.data[2 * i], self.data[2 * i + 1])

    def __len__(self):
        return self._len

    def _push(self, idx):
        """Push pending assignments at idx to its children."""
        if self._lazy[idx] is not None:
            self.data[2 * idx] = self._lazy[idx]
            self.data[2 * idx + 1] = self._lazy[idx]
            self._lazy[2 * idx] = self._lazy[idx]
            self._lazy[2 * idx + 1] = self._lazy[idx]
            self._lazy[idx] = None

    def _update(self, idx):
        """Update the node idx to apply all pending assignments from ancestors."""
        for i in reversed(range(1, idx.bit_length())):
            self._push(idx >> i)

    def _build(self, idx):
        """Update ancestors of idx to reflect the changes."""
        idx >>= 1
        while idx:
            if self._lazy[idx] is None:
                self.data[idx] = self._func(self.data[2 * idx], self.data[2 * idx + 1])
            else:
                self.data[idx] = self._lazy[idx]
            idx >>= 1

    def assign(self, start, stop, value):
        """Assign value to the range [start, stop)."""
        start = start_copy = start + self._size
        stop = stop_copy = stop + self._size
        while start < stop:
            if start & 1:
                self.data[start] = value
                self._lazy[start] = value
                start += 1
            if stop & 1:
                stop -= 1
                self.data[stop] = value
                self._lazy[stop] = value
            start >>= 1
            stop >>= 1
        self._build(start_copy)
        self._build(stop_copy - 1)

    def query(self, start, stop, default=0):
        """Return the max value in data[start, stop)."""
        start += self._size
        stop += self._size
        self._update(start)
        self._update(stop - 1)

        res = default
        while start < stop:
            if start & 1:
                res = self._func(res, self.data[start])
                start += 1
            if stop & 1:
                stop -= 1
                res = self._func(res, self.data[stop])
            start >>= 1
            stop >>= 1
        return res

    def __repr__(self):
        return "LazySegmentTree({0})".format(self.data[self._size:self._size + self._len])


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

