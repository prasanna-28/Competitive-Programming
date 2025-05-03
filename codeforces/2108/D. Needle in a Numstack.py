import sys, math
from collections import deque, defaultdict, Counter

MOD       = 10**9 + 7
FASTIO    = False
DEBUG     = False
INF       = float('inf')
NINF      = float('-inf')
YES, NO   = "YES", "NO"
MT        = True

def query(x):
    print("?", x, flush = True)
    return int(input())
#====================Solution====================

def sol():
    n, k = ivars()

    fk = [query(i) for i in range(1, k + 1)]

    r = n % k
    tail = n - r - k + 1
    lk = [query(tail + i) for i in range(k)]

    if fk == lk:
        if n == 2 * k:
            print('!', k, k, flush=True)
        else:
            print('! -1', flush=True)
        return

    d = next(i for i in range(k) if fk[i] != lk[i])
    base = fk[d]

    lo, hi = d + 1, n - k + d + 1
    while hi - lo > k:
        mid = lo + ((hi - lo) // (2 * k)) * k
        (lo, hi) = (mid, hi) if query(mid) == base else (lo, mid)

    win = list(range(lo, hi))
    vals = [query(x) for x in win]

    ok = []
    for shift, s in enumerate(win[:-1]):
        if s < k or n - s < k:
            continue
        a_tail = vals[shift - k + 1:shift + 1]
        b_head = vals[shift + 1:shift + k + 1]
        if len(set(a_tail)) == k and len(set(b_head)) == k:
            ok.append(s)

    if len(ok) == 1:
        print('!', ok[0], n - ok[0], flush=True)
    else:
        print('! -1', flush=True)
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

