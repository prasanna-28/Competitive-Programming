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
    n = ipt()
    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = ivars()
        adj[u].append(v)
        adj[v].append(u)
    s = ' ' + input()
    leaves = []
    ones = zeros = 0
    for i in range(n + 1):
        if len(adj[i]) == 1 and i != 1 and s[i] == '?':
            leaves.append(i)
        elif len(adj[i]) == 1 and i != 1:
            if s[i] == '1':
                ones += 1
            else:
                zeros += 1
    news = ['0'] * (n + 1)
    for i in range(1, n + 1):
        news[i] = s[i]
    for i in leaves:
        news[i] = '0'
    news[1] = '0'
    dummy = 0
    res = max(ones, zeros) + len(leaves)//2

    for i in news:
        if i == '?':
            dummy += 1

    if s[1] == '?':
        if ones == zeros and dummy & 1 and len(leaves) & 1:
            print(res + 1)
        else:
            print(res)
    else:
        if len(leaves) & 1:
            print((len(leaves) + 1)//2 + (zeros if s[1] == '1' else ones))
        else:
            print(len(leaves)//2 + (zeros if s[1] == '1' else ones))

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

