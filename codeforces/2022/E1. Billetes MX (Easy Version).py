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
MOD = 10**9 + 7

def is_beautiful(n, m, rc):
    from collections import defaultdict

    # Each cell's value is represented as a 30-bit integer
    equations = []
    for r, c, v in rc:
        equation = [0] * (n + m)
        equation[r - 1] = 1  # Row variable
        equation[n + c - 1] = 1  # Column variable
        equations.append((equation, v))

    # Perform Gaussian elimination over GF(2) for each bit
    for bit in range(30):
        eq = []
        for equation, value in equations:
            eq.append((equation[:], (value >> bit) & 1))

        rank = 0
        for i in range(n + m):
            pivot = -1
            for j in range(rank, len(eq)):
                if eq[j][0][i]:
                    pivot = j
                    break
            if pivot == -1:
                continue
            eq[rank], eq[pivot] = eq[pivot], eq[rank]
            for j in range(len(eq)):
                if j != rank and eq[j][0][i]:
                    eq[j] = ([x ^ y for x, y in zip(eq[j][0], eq[rank][0])], eq[j][1] ^ eq[rank][1])
            rank += 1

        for j in range(rank, len(eq)):
            if eq[j][1] != 0:
                return False
    return True

def sol():
    import sys
    import sys
    input = sys.stdin.read
    data = input().split()
    idx = 0
    t = int(data[idx]); idx +=1
    for _ in range(t):
        n = int(data[idx]); m = int(data[idx+1]); k = int(data[idx+2]); q = int(data[idx+3]); idx +=4
        rc = []
        cols = set()
        rows = set()
        for __ in range(k):
            r = int(data[idx]); c = int(data[idx+1]); v = int(data[idx+2]); idx +=3
            rc.append((r, c, v))
            if r == 1:
                cols.add(c)
            else:
                rows.add(r)
        if is_beautiful(n, m, rc):
            f = n + m - len(cols) - len(rows) -1
            if f <0:
                print(0)
            else:
                print(pow(2, 30*f, MOD))
        else:
            print(0)

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

