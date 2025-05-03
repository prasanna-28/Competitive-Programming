import sys, math
from collections import deque, defaultdict, Counter

MOD       = 10**9 + 7
FASTIO    = False
DEBUG     = False
INF       = float('inf')
NINF      = float('-inf')
YES, NO   = "YES", "NO"
MT        = not True
from bisect import bisect_right
#====================Solution====================
def sol():
    ns = []
    mx = 0
    for i in range(ipt()):
        ns.append(ipt())
        mx = max(mx, ns[-1])

    best = {}
    p10 = [10**i for i in range(12)]
    for t9 in range(1, 10):
        x = pow(10, t9) - 1
        if x <= mx:
            c0 = [0]*10
            for d in str(x):   c0[int(d)] += 1
            d0 = [0]*10
            for d in str(x+1): d0[int(d)] += 1
            u = tuple(c0[i] + d0[i] for i in range(10))
            if u in best:
                if x < best[u]: best[u] = x
            else:
                best[u] = x

    c = [0]*10
    for L in range(1, 10):
        for i in range(10): c[i] = 0
        c[0] = L

        while True:
            for p in range(9):
                if c[p] > 0:
                    c9 = c[9]
                    for t9 in range(c9+1):
                        sp = L - t9 - 1
                        cp = c.copy()
                        cp[9] -= t9
                        cp[p] -= 1

                        pr = []
                        if sp > 0:
                            for d in range(1, 10):
                                if cp[d]:
                                    pr.append(d)
                                    cp[d] -= 1
                                    break
                            pr += [0]*cp[0]
                            for d in range(1, 10):
                                pr += [d]*cp[d]

                        pm = 0
                        for d in pr:
                            pm = pm*10 + d

                        if t9 > 0:
                            x = pm*p10[t9+1] + p*p10[t9] + (p10[t9] - 1)
                        else:
                            x = pm*10 + p

                        if 1 <= x <= mx:
                            c0 = [0]*10
                            for d in str(x):   c0[int(d)] += 1
                            d0 = [0]*10
                            for d in str(x+1): d0[int(d)] += 1
                            u = tuple(c0[i] + d0[i] for i in range(10))
                            if u in best:
                                if x < best[u]: best[u] = x
                            else:
                                best[u] = x

            idx = -1
            for j in range(8, -1, -1):
                if c[j] > 0:
                    idx = j
                    break
            if idx < 0:
                break

            c[idx] -= 1
            sumr = 1
            for j in range(idx+1, 10):
                sumr += c[j]
                c[j] = 0
            c[idx+1] = sumr
    best = sorted(best.values())
    for n in ns:
        print(bisect_right(best, n))

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

