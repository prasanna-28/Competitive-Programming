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
    a = [0] + ilist() + [0]
    d = [INF] + ilist() + [INF]
    poss = deque()
    dsu = DSU(n+2)
    for i in range(1, n + 1):
        if a[i - 1] + a[i + 1] > d[i]:
            poss.append(i)
    deleted = set()

    ans = []
    for _ in range(n):
        new_poss = deque()
        delet = []

        while poss:
            i = poss.popleft()
            if i in deleted: continue
            left = dsu.get(dsu.left[i])
            right = dsu.get(dsu.right[i])
            if i == 0 or i == n + 1: continue
            if a[left] + a[right] > d[i]:
                delet.append(i)
                new_poss.append(left)
                new_poss.append(right)
        ans.append(len(delet))
        for i in delet:
            dsu.delete(i)
            deleted.add(i)
        poss = new_poss


    print(*ans)


class DSU:
    def __init__(self, n):
        self.p = list(range(n + 2))
        self.r = [1] * (n + 2)
        self.left = [i-1 for i in range(n + 2)]
        self.right = [i+1 for i in range(n + 2)]

    def get(self, a):
        if self.p[a] != a:
            self.p[a] = self.get(self.p[a])
        return self.p[a]

    def delete(self, a):
        a = self.get(a)
        self.right[self.get(self.left[a])] = self.get(self.right[a])
        self.left[self.get(self.right[a])] = self.get(self.left[a])






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

