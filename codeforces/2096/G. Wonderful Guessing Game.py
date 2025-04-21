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
    n = ipt()
    d = 0
    p = 1
    while p < n:
        p *= 3
        d += 1
    q = d + 1
    dig = [[0] * q for _ in range(n)]
    for i in range(n):
        v = i
        for j in range(d):
            dig[i][j] = v % 3
            v //= 3
    for j in range(d):
        g0 = [i for i in range(n) if dig[i][j] == 0]
        g1 = [i for i in range(n) if dig[i][j] == 1]
        m = min(len(g0), len(g1))
        for i in g0[m:]:
            dig[i][j] = 2
        for i in g1[m:]:
            dig[i][j] = 2
    for i in range(n):
        s = sum(dig[i][:d]) % 3
        dig[i][d] = (-s) % 3
    codes = [''] * n
    queries = []
    for j in range(q):
        arr = []
        for i in range(n):
            if dig[i][j] == 0:
                arr.append(i + 1)
        for i in range(n):
            if dig[i][j] == 1:
                arr.append(i + 1)
        queries.append(arr)
        for i in range(n):
            codes[i] += "LRN"[dig[i][j]]
    print(q, flush=True)
    for arr in queries:
        print(len(arr), *arr, flush=True)
    s = input()
    ig = s.find('?')
    ans = 1
    for i, pat in enumerate(codes):
        ok = True
        for j, ch in enumerate(pat):
            if j == ig:
                continue
            if ch != s[j]:
                ok = False
                break
        if ok:
            ans = i + 1
            break
    print(ans, flush=True)

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

