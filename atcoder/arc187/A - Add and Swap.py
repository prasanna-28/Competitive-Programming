import sys, math
from collections import deque, defaultdict, Counter

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
    res = []
    if n == 2:
        if a == sorted(a):
            print('Yes')
            print(0)
            return
        a[0], a[1] = a[1] + k, a[0]
        if a == sorted(a):
            print('Yes')
            print(1)
            print(1)
            return
        print('No')
        return

    while a[1] < a[0] + 3 * k:
        a[1] += k
        a[2] += k
        res.append(2)
        res.append(2)
    while a[1] < a[2] + 3 * k:
        a[1] += k
        a[0] += k
        res.append(1)
        res.append(1)
    while a[2] < a[0] + 4 * k:
        a[1] += k
        a[2] += k
        res.append(2)
        res.append(2)
    a[1], a[2] = a[2] + k, a[1]
    res.append(2)
    for i in range(3, len(a)):
        idx = i
        while idx > 0:
            a[idx - 1], a[idx] = a[idx] + k, a[idx - 1]
            idx -= 1
            res.append(idx + 1)
        for x in range(1, i, 2):
            mx = max(a[:x])
            while a[x] < mx:
                res.append(x + 1)
                res.append(x + 1)
                a[x] += k
                a[x + 1] += k
        if not i & 1:
            while a[i - 1] < a[i - 2] + 3 * k:
                a[i - 1] += k
                a[i] += k
                res.append(i)
                res.append(i)
            while a[i - 1] < a[i] + 3 * k:
                a[i - 1] += k
                a[i - 2] += k
                res.append(i - 1)
                res.append(i - 1)
            while a[i] < a[i - 2] + 4 * k:
                a[i - 1] += k
                a[i] += k
                res.append(i)
                res.append(i)
            a[i - 1], a[i] = a[i] + k, a[i - 1]
            res.append(i)
    if a != sorted(a):
        print('No')
        return
    print('Yes')
    print(len(res))
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

