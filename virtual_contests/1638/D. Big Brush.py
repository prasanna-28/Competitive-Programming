import sys, math
from collections import deque
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
#=============================================#
def sol():
    n,m = ivars()
    grid = [[0]*m for _ in range(n)]
    for i in range(n):
        grid[i] = list(map(int, input().split()))
    start = []
    for i in range(n-1):
        for j in range(m-1):
            if grid[i][j] == grid[i+1][j] == grid[i][j+1] == grid[i+1][j+1]:
                start.append((i,j))
    if start == []:
        print(-1)
        return

    def check(i, j):
        if i+1 >= n or j + 1 >= m: return False
        nums = [grid[i][j], grid[i+1][j], grid[i][j+1], grid[i+1][j+1]]
        for x in nums:
            if x != -1:
                new = x
                break
        else:
            return False
        return all(x == new or x == -1 for x in nums)


    q = deque(start)
    res = []

    while q:
        i,j = q.popleft()
        c = -1
        if ~grid[i][j]:
            c = grid[i][j]
            grid[i][j] = -1
        elif ~grid[i+1][j]:
            c = grid[i+1][j]
            grid[i+1][j] = -1
        elif ~grid[i+1][j+1]:
            c = grid[i+1][j+1]
            grid[i+1][j+1] = -1
        elif ~grid[i][j+1]:
            c = grid[i][j+1]
            grid[i][j+1] = -1
        else:
            continue

        res.append((i+1, j+1, c))

        grid[i][j] = -1
        grid[i+1][j] = -1
        grid[i][j+1] = -1
        grid[i+1][j+1] = -1
        if check(i+1, j):
            q.append((i+1, j))
        if check(i, j + 1):
            q.append((i, j + 1))
        if check(i+1, j+1):
            q.append((i+1, j+1))
        if i > 0 and j > 0:
            if check(i-1, j-1):
                q.append((i-1, j-1))
        if i > 0:
            if check(i-1, j):
                q.append((i-1, j))
            if check(i-1, j + 1):
                q.append((i-1, j+1))
        if j > 0:
            if check(i, j-1):
                q.append((i, j-1))
            if check(i+1, j - 1):
                q.append((i+1, j-1))

    for i in grid:
        for j in i:
            if ~j:
                print(-1)
                return
    print(len(res))
    for t in reversed(res):
        i, j, c = t
        sys.stdout.write(f"{i} {j} {c}\n")




#=============================================#


if __name__ == "__main__":
    #for _ in range(ipt()): sol()
    finp   = sys.stdin.readline
    MOD    = 10**9 + 7
    njoin  = lambda x: '\n'.join(map(str, x))
    ljoin  = lambda x: ' '.join(map(str, x))
    sjoin  = lambda x: '\n'.join(x)
    initl  = lambda x,y: [y]*x
    INF    = float('inf')
    NINF   = float('-inf')
    ilist  = lambda: list(map(int, finp().split()))
    slist  = lambda: list(input())
    slists = lambda: input().split()
    ivars  = lambda: map(int, finp().split())
    ipt    = lambda: int(finp())
    out    = []
    sol()
    pass


'''
xxxxxx
xxxxxx
xxaaxx
xxaaxx
xxxxxx
xxxxxx
'''






