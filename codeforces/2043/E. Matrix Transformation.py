import sys, math
from collections import deque, defaultdict, Counter

MOD       = 10**9 + 7
FASTIO    = True
DEBUG     = False
INF       = float('inf')
NINF      = float('-inf')
YES, NO   = "YES", "NO"
MT        = True
MAX_BIT = 31

#====================Solution====================
def sol():
    n, m = ivars()
    A = [ilist() for _ in range(n)]
    B = [ilist() for _ in range(n)]
    MAX_BIT = 31

    def can_transform_bit(bit):
        rowBit = [-1]*n
        colBit = [-1]*m
        changed = True
        while changed:
            changed = False
            for i in range(n):
                for j in range(m):
                    a = (A[i][j] >> bit) & 1
                    b = (B[i][j] >> bit) & 1
                    rb = rowBit[i]
                    cb = colBit[j]
                    if a == 0 and b == 1:
                        if cb == 0:
                            return False
                        if cb == -1:
                            colBit[j] = 1
                            changed = True
                    elif a == 0 and b == 0:
                        if cb == 1:
                            return False
                        if cb == -1:
                            colBit[j] = 0
                            changed = True
                    elif a == 1 and b == 0:
                        if cb == 1:
                            return False
                        if cb == -1:
                            colBit[j] = 0
                            changed = True
                        if rb == 1:
                            return False
                        if rb == -1:
                            rowBit[i] = 0
                            changed = True
                    else:
                        if rb == 0 and cb == 0:
                            return False
                        if rb == 0 and cb == -1:
                            colBit[j] = 1
                            changed = True
                        if rb == -1 and cb == 0:
                            rowBit[i] = 1
                            changed = True
        return True

    ok = True
    for bit in range(MAX_BIT):
        if not can_transform_bit(bit):
            ok = False
            break
    print("Yes" if ok else "No")









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

