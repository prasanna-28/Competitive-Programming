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

def sol(l, r):
    #l, r = ivars()
    b = list(range(l, r + 1))
    n = r - l + 1
    def build(swap_right):
        res = [0] * n
        st = [(list(range(n)), b[:], 29)]
        while st:
            ps, vs, k = st.pop()
            if not ps:
                continue
            if k < 0:
                for i, v in zip(ps, vs):
                    res[i] = v
                continue
            tl, tr = [], []
            for i in ps:
                if (b[i] >> k) & 1: tr.append(i)
                else: tl.append(i)
            a0, a1 = [], []
            for v in vs:
                if (v >> k) & 1: a1.append(v)
                else: a0.append(v)
            m = len(tl)
            x = min(len(a1), m)
            gl = a1[:x] + a0[:m - x]
            if swap_right:
                gr = a1[x:] + a0[m - x:]
            else:
                gr = a0[m - x:] + a1[x:]
            st.append((tr, gr, k - 1))
            st.append((tl, gl, k - 1))
        s = 0
        for i in range(n):
            s += res[i] | b[i]
        return s, res
    s1, r1 = build(False)
    s2, r2 = build(True)
    if s2 > s1:
        return s2, r2
        print(s2)
        print(ljoin(r2))
    else:
        return s1, r1
        print(s1)
        print(ljoin(r1))




#================================================
import itertools
import random
def brute(l, r):
    b = list(range(l, r + 1))
    a = b[:]
    best = -1
    pr = b[:]
    for p in itertools.permutations(a):
        s = 0
        for i in range(len(b)):
            s += p[i] | b[i]
        if s > best:
            best = s
            pr = p
    res = []
    for p in itertools.permutations(a):
        s = 0
        for i in range(len(b)):
            s += p[i] | b[i]
        if s == best:
            best = s
            res.append(p)
    return best, res

def generate_test():
    l = random.randint(0, (1 << 6) - 12)
    return l, l + (random.randint(5, 8))

def main():
    #'''
    for i in range(1000):
        l,r = generate_test()
        print(list(range(l, r + 1)))
        a, res = brute(l, r)
        print(a)
        for i in res:
            print(i)
        print()
        print()
    #'''
    return
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

