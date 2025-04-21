import sys, math
from collections import deque, defaultdict, Counter

MOD       = 10**9 + 7
FASTIO    = False
DEBUG     = False
INF       = float('inf')
NINF      = float('-inf')
YES, NO   = "YES", "NO"
MT        = not True
from heapq import heappush as hpush, heappop as hpop
#====================Solution====================
def sol():
    h, w = ivars()
    grid = []
    for _ in range(h):
        grid.append(list(input()))
    a, b, c, d = ivars()
    a-= 1
    b-=1
    c-=1
    d -=1
    dist = [[INF] * w for _ in range(h)]
    dq = deque()
    dist[a][b] = 0
    dq.append((a, b))

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while dq:
        i, j = dq.popleft()
        current_dist = dist[i][j]
        if i == c and j == d:
            print(current_dist)
            return

        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < h and 0 <= nj < w:
                if grid[ni][nj] == '.' and dist[ni][nj] > current_dist:
                    dist[ni][nj] = current_dist
                    dq.appendleft((ni, nj))

        for di, dj in directions:
            steps = []
            for step in 1, 2:
                ni = i + di * step
                nj = j + dj * step
                if 0 <= ni < h and 0 <= nj < w:
                    if grid[ni][nj] == '#':
                        grid[ni][nj] = '.'  # Convert to road
                    steps.append((ni, nj))
                else:
                    break
            for step in 1, 2:
                ni = i + di * step
                nj = j + dj * step
                if 0 <= ni < h and 0 <= nj < w and dist[ni][nj] > current_dist + 1:
                    dist[ni][nj] = current_dist + 1
                    dq.append((ni, nj))

    print(-1)
    



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

