
import sys, math
from collections import deque, defaultdict, Counter
from bisect import bisect_left

MOD       = 10**9 + 7
FASTIO    = False
DEBUG     = False
INF       = float('inf')
NINF      = float('-inf')
YES, NO   = "YES", "NO"
MT        = False

#====================Solution====================
def sol():
    n, k = ivars()
    a = ilist()
    bigger = [0] * len(a)
    res = [0] * len(a)
    prev = [[i] for i in a]
    for i in range(n):
        newprev = []
        idx = 0
        for j in range(0, len(prev)//2):
            merge1 = prev[2*j]
            merge2 = prev[2*j + 1]
            new = []
            numsmaller = defaultdict(int)
            p1 = 0
            p2 = 0
            while p1 < len(merge1) and p2 < len(merge2):
                if merge1[p1] > merge2[p2]:
                    new.append(merge2[p2])
                    numsmaller[merge2[p2]] = len(new)
                    p2 += 1
                else:
                    new.append(merge1[p1])
                    numsmaller[merge1[p1]] = len(new)
                    p1 += 1
            while p1 < len(merge1):
                new.append(merge1[p1])
                numsmaller[merge1[p1]] = len(new)
                p1 += 1
            while p2 < len(merge2):
                new.append(merge2[p2])
                numsmaller[merge2[p2]] = len(new)
                p2 += 1
            newprev.append(new)
            for _ in range(len(new)):
                bigger[idx] = len(new) - numsmaller[a[idx]]
                if bigger[idx] <= k and a[idx] >= len(new):
                    res[idx] += 1
                idx += 1
        prev = newprev
    print(ljoin(res))


def solv():
    n, k = ivars()
    a = ilist()
    bigger = [0] * len(a)
    prev = [[i] for i in a]
    for i in range(n):
        idx = 0
        for group in range(0, len(a), (u:=pow(2, i + 1))):
            curr = a[group:group + u]
            curr.sort()
            for _ in range(len(curr)):
                bigger[i][idx] = u - bisect_left(curr, a[idx]) - 1
                idx += 1
    res = [0] * len(a)
    for i in range(len(a)):
        for j in range(len(bigger)):
            if bigger[j][i] <= k and a[i] >= pow(2, j + 1):
                res[i] += 1
    print(ljoin(res))



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

