import sys, math
from collections import deque, defaultdict, Counter
from bisect import bisect_left, bisect_right
MOD       = 10**9 + 7
FASTIO    = False
DEBUG     = False
INF       = float('inf')
NINF      = float('-inf')
YES, NO   = "YES", "NO"
MT        = True

#====================Solution====================
def minc(N):

    adj = [[] for i in range(N)]

    count = [0]*N
    colors = [1]*(N)

    for i in range(1, N + 1):
        for j in range(1, i):
            if i ^ j in primes:
                adj[j - 1].append(i - 1)
                count[j - 1] += 1

    Q = deque()

    for i in range(N):
        if (count[i] == 0):
            Q.append(i)

    while len(Q) > 0:
        u = Q.popleft()

        # Traverse node u
        for x in adj[u]:
            count[x] -= 1

            # If count[x] = 0
            # insert in Q
            if (count[x] == 0):
                Q.append(x)

            # If colors of child
            # node is less than
            # parent node, update
            # the count by 1
            if (colors[x] <= colors[u]):
                colors[x] = 1 + colors[u]

    # requires to color the graph.
    minColor = -1

    # Find the maximum of colors[]
    for i in range(N):
        minColor = max(minColor, colors[i])

    # Print the minimum no. of
    # colors required.
    print(minColor)
    print(colors)

def greed_sol(n):
    minc(500)

def brute_sol(n):
    colors = [0] * (n + 1)
    col = 0
    for i in range(1, n + 1):
        mex = set()
        for j in primes:
            if 0 < i ^ j <= n:
                mex.add(colors[i ^ j])
        c = 1
        while c in mex:
            c += 1
        col = max(col, c)
        colors[i] = c
    print(col)
    print(colors[1:])

def sol(n):
    if n == 1:
        print(1)
        print(1); return
    if n == 2:
        print(2)
        print(1, 2); return
    if n == 3:
        print(2)
        print(1, 2, 2); return
    if n == 4:
        print(3)
        print(1, 2, 2, 3); return
    if n == 5:
        print(3)
        print(1 ,2 ,2 ,3 ,3)
        return
    if n == 6:
        print(4)
        print(1, 2, 2, 3, 3, 4); return
    print(4)
    for i in range(1, n + 1):
        print(i % 4 + 1, end = ' ')
    print('\n', end = '')

#================================================

def main():
    for _ in range(ipt() if MT else 1):
        n = ipt()
        sol(n)


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

