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
    n, m = ivars()
    grid = [input() for _ in range(n)]
    seen = set()
    q = deque()
    for i in range(m):
        if grid[0][i] == 'U' and (0, i) not in seen:
            q.append((0, i))
            seen.add((0, i))
        if grid[n - 1][i] == 'D' and (n - 1, i) not in seen:
            q.append((n - 1, i))
            seen.add((n - 1, i))
    for i in range(n):
        if grid[i][0] == 'L' and (i, 0) not in seen:
            q.append((i, 0))
            seen.add((i, 0))
        if grid[i][m - 1] == 'R' and (i, m - 1) not in seen:
            q.append((i, m - 1))
            seen.add((i, m - 1))
    dirs = [(1, 0, 'U'), (-1, 0, 'D'), (0, 1, 'L'), (0, -1, 'R')]
    while q:
        x, y = q.popleft()
        for dx, dy, k in dirs:
            if n > x + dx >= 0 and m > y + dy >= 0:
                ix, iy = x + dx, y + dy
                if grid[ix][iy] == k and (ix, iy) not in seen:
                    q.append((ix, iy))
                    seen.add((ix, iy))

    curr = (n * m) - len(seen)
    for i in range(n):
        for j in range(m):
            if (i, j) in seen or grid[i][j] != '?': continue
            for dx, dy, _ in dirs:
                if n > i + dx >= 0 and m > j + dy >= 0:
                    if (i + dx, j + dy) not in seen:
                        break
            else:
                curr -= 1
    print(curr)

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

