import sys, math
from collections import deque, defaultdict, Counter
from functools import cache
MOD       = 10**9 + 7
FASTIO    = True
DEBUG     = False
INF       = float('inf')
NINF      = float('-inf')
YES, NO   = "YES", "NO"
MT        = False

#====================Solution====================
@cache
def factorize(x):
    out = []
    for i in range(2, math.isqrt(x) + 2):
        if not x % i:
            out.append(i)
            while not x % i:
                x //= i
        if x == 1:
            break
    if x != 1:
        out.append(x)
    return out

def main():
    n = ipt()
    a = ilist()
    s, t = ivars()
    if s == t:
        print(1)
        print(s)
        return
    if a[s-1] == a[t-1] and a[s-1] != 1:
        print(2)
        print(s, t)
        return
    s, t = s-1, t-1
    factors = [[] for _ in range(300001)]
    seen = [False] * (max(a) + 1)
    for i, v in enumerate(a):
        if seen[v] or (i != t and v == a[t]): continue
        seen[v] = True
        for k in factorize(v):
            factors[k].append(i)
    seen = set()
    p = [-1] * n
    q = deque([s])
    seen.add(a[s])
    factor_seen = set()
    while q:
        curr = q.popleft()
        if curr == t: break
        for factor in factorize(a[curr]):
            if factor in factor_seen: continue
            for child in factors[factor]:
                if a[child] in seen: continue
                seen.add(a[child])
                p[child] = curr
                q.append(child)
            factor_seen.add(factor)
    else:
        print(-1)
        return
    path = []
    while t != -1:
        path.append(t + 1)
        t = p[t]
    print(len(path))
    for i in range(len(path) -1, -1, -1):
        print(path[i], end = ' ')
    print()

#================================================


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


