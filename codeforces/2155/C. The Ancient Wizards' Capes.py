import sys, math
from collections import deque, defaultdict, Counter

MOD       = 676767677
FASTIO    = False
DEBUG     = False
INF       = float('inf')
NINF      = float('-inf')
YES, NO   = "YES", "NO"
MT        = True

#====================Solution====================
def sol():
    n = ipt()
    a = ilist()
    if len(set(a)) == 1:
        if n & 1:
            if a[0] == (n + 1)//2:
                print(2)
                return
        else:
            if a[0] == n//2 or a[0] == n//2 + 1:
                print(1)
                return
        print(0)
        return
    parens = [0] * n
    for i in range(1, n):
        if a[i - 1] < a[i]:
            if parens[i - 1] == 1 or parens[i] == 1:
                print(0)
                return
            parens[i - 1] = -1
            parens[i] = -1
            c = i - 2
            while c >= 0 and parens[c] == 0:
                parens[c] = 1 if parens[c + 1] == -1 else -1
                c -= 1
        elif a[i - 1] > a[i]:
            if parens[i - 1] == -1 or parens[i] == -1:
                print(0)
                return
            parens[i - 1] = 1
            parens[i] = 1 
            c = i - 2
            while c >= 0 and parens[c] == 0:
                parens[c] = 1 if parens[c + 1] == -1 else -1
                c -= 1

    i = n - 1
    while parens[i] == 0:
        i -= 1

    i += 1
    while i < n:
        parens[i] = 1 if parens[i - 1] == -1 else -1
        i += 1

    res1 = []
    res2 = []
    for i in range(n):
        if parens[i] == 1:
            res1.append(1)
            res2.append(0)
        else:
            res2.append(1)
            res1.append(0)

    for i in range(1, n):
        res2[i] += res2[i - 1]
        res1[n - i - 1] += res1[n - i]
    for i in range(n):
        if res1[i] + res2[i] != a[i]:
            print(0)
            return
    print(1)


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

