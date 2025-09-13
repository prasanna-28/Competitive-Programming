import sys, math
from collections import deque, defaultdict, Counter

MOD       = 10**9 + 7
FASTIO    = False
DEBUG     = False
INF       = float('inf')
NINF      = float('-inf')
YES, NO   = "YES", "NO"
MT        =not  True

#====================Solution====================
def sol():
    n, m, k = ivars()
    a = ilist()
    a.reverse()
    b = 0
    s = 0
    ct = 0
    curr = []
    res = []
    for idx, i in enumerate(a):
        if s + i > k:
            b += 1
            s = i
            res.append(curr)
            curr = [i]
        else:
            s += i
            curr.append(i)
    res.append(curr)
    ans =0 
    for i in range(min(m, len(res))):
        ans += len(res[i])
    print(ans)
def sol2():
    n, m, k = ivars()
    a = ilist()
    p = [0]
    for i in a:
        p.append(p[-1] + i)
    dp = [0] * (n + 1)
    def bs(i):
        l = 1 << 20
        res = 0
        while l > 0:
            cand = res | l
            if i - cand < 0:
                l >>= 1
                continue
            prev = p[i - cand]
            curr = p[i]
            if curr - prev <= k:
                res |= l
            l >>= 1
    for i in range(n):
        curr = a[i]
        dpi = i + 1
        prev = bs(dpi)
        dp[dpi] = dp[prev] + dp[i] - prev + 1
    print(dp[-1])



def sol1():
    n, m, k = ivars()
    a = ilist()
    l = 0
    r = n + 1
    def cond(i):
        if i >= n:
            return False
        new = a[i:]
        boxes = 0
        s = 0
        for i in new:
            if s + i > m:
                boxes += 1
                s = i
            else:
                s += i
        if s != 0:
            boxes += 1
        return boxes <= m
    res = 0
    l = 1 << 20
    while l > 0:
        cand = res | l
        if cond(cand):
            res = cand
        l >>= 1

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

