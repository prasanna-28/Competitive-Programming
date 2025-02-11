import sys, math
from collections import deque, defaultdict, Counter
import operator
MOD       = 988_244_353
FASTIO    = False
DEBUG     = False
INF       = float('inf')
NINF      = float('-inf')
YES, NO   = "YES", "NO"
MT        = True

#====================Solution====================
def sol():
    s = list(input().strip())
    q = ipt()
    v = ilist()
    n = len(s)
    L = [1] * n
    for i in range(1, n):
        L[i] = (L[i-1] * 2) % MOD
    R = [1] * n
    R[n-1] = 1
    for i in range(n-2, -1, -1):
        R[i] = (R[i+1] * 2) % MOD
    const = (pow(2, n, MOD) - 1) % MOD
    s_0l = Fenw(n)
    s_1l = Fenw(n)
    s_0r = Fenw(n)
    s_1r = Fenw(n)
    for i in range(n):
        if s[i] == '0':
            s_0l.update(i, L[i])
            s_0r.update(i, R[i])
        else:
            s_1l.update(i, L[i])
            s_1r.update(i, R[i])
    res = 0
    for i in range(n):
        if s[i] == '0':
            res = (res + L[i] * s_1r.query(i+1, n)) % MOD
        else:
            res = (res + L[i] * s_0r.query(i+1, n)) % MOD
    total = []
    for x in v:
        x -= 1
        if s[x] == '1':
            left_diff = (s_1l.query(0, x) - s_0l.query(0, x)) % MOD
            right_diff = (s_1r.query(x+1, n) - s_0r.query(x+1, n)) % MOD
            diff = (R[x] * left_diff + L[x] * right_diff) % MOD
            res = (res + diff) % MOD
            s_1l.update(x, (-L[x]) % MOD)
            s_1r.update(x, (-R[x]) % MOD)
            s_0l.update(x, L[x])
            s_0r.update(x, R[x])
            s[x] = '0'
        else:
            left_diff = (s_0l.query(0, x) - s_1l.query(0, x)) % MOD
            right_diff = (s_0r.query(x+1, n) - s_1r.query(x+1, n)) % MOD
            diff = (R[x] * left_diff + L[x] * right_diff) % MOD
            res = (res + diff) % MOD
            s_0l.update(x, (-L[x]) % MOD)
            s_0r.update(x, (-R[x]) % MOD)
            s_1l.update(x, L[x])
            s_1r.update(x, R[x])
            s[x] = '1'
        total.append((res + const) % MOD)
    print(ljoin(total))
#================================================

class Fenw:
    def __init__(self, n):
        self.n = n
        self.fw = [0]*(n+1)
    def update(self, i, delta):
        i += 1
        while i <= self.n:
            self.fw[i] = (self.fw[i] + delta) % MOD
            i += i & -i
    def query(self, l, r):
        return (self._query(r) - self._query(l)) % MOD
    def _query(self, i):
        s = 0
        while i:
            s = (s + self.fw[i]) % MOD
            i -= i & -i
        return s

class SegmentTree:
    def __init__(self, data, default=0, func=max):
        """initialize the segment tree with data"""
        self._default = default
        self._func = func
        self._len = len(data)
        self._size = _size = 1 << (self._len - 1).bit_length()

        self.data = [default] * (2 * _size)
        self.data[_size:_size + self._len] = data
        for i in reversed(range(_size)):
            self.data[i] = func(self.data[i + i], self.data[i + i + 1])

    def __delitem__(self, idx):
        self[idx] = self._default

    def __getitem__(self, idx):
        return self.data[idx + self._size]

    def __setitem__(self, idx, value):
        idx += self._size
        self.data[idx] = value
        idx >>= 1
        while idx:
            self.data[idx] = self._func(self.data[2 * idx], self.data[2 * idx + 1])
            idx >>= 1

    def __len__(self):
        return self._len

    def query(self, start, stop):
        """func of data[start, stop)"""
        start += self._size
        stop += self._size

        res_left = res_right = self._default
        while start < stop:
            if start & 1:
                res_left = self._func(res_left, self.data[start])
                start += 1
            if stop & 1:
                stop -= 1
                res_right = self._func(self.data[stop], res_right)
            start >>= 1
            stop >>= 1

        return self._func(res_left, res_right)

    def __repr__(self):
        return "SegmentTree({0})".format(self.data)
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

