import sys, math
from collections import deque, defaultdict, Counter

MOD       = 10**9 + 7
FASTIO    = False
DEBUG     = False
INF       = float('inf')
NINF      = float('-inf')
YES, NO   = "YES", "NO"
MT        = True

#====================Solution====================
def sol():
    n = ipt()
    q = ipt()
    for _ in range(q):
        a = input().split(' ')
        if a[0] == '->':
            x = int(a[1])
            y = int(a[2])
            res = 1
            lev = n
            xx, yy = x, y
            while lev > 1:
                hlf = 1 << (lev - 1)
                qsz = hlf * hlf
                if xx <= hlf and yy <= hlf:
                    pass
                elif xx > hlf and yy > hlf:
                    xx -= hlf
                    yy -= hlf
                    res += qsz
                elif xx > hlf and yy <= hlf:
                    xx -= hlf
                    res += 2 * qsz
                else:
                    yy -= hlf
                    res += 3 * qsz
                lev -= 1
            if xx == 1 and yy == 1:
                print(res)
            elif xx == 2 and yy == 2:
                print(res + 1)
            elif xx == 2 and yy == 1:
                print(res + 2)
            else:
                print(res + 3)
        else:
            d = int(a[1])
            lev = n
            dd = d - 1
            rx, ry = 1, 1
            while lev > 1:
                hlf = 1 << (lev - 1)
                qsz = hlf * hlf
                idx = dd // qsz
                dd %= qsz
                if idx == 0:
                    pass
                elif idx == 1:
                    rx += hlf
                    ry += hlf
                elif idx == 2:
                    rx += hlf
                else:
                    ry += hlf
                lev -= 1
            if dd == 0:
                print(rx, ry)
            elif dd == 1:
                print(rx + 1, ry + 1)
            elif dd == 2:
                print(rx + 1, ry)
            else:
                print(rx, ry + 1)

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

