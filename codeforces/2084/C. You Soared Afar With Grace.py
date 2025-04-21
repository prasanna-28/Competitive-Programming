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
    a = ilist()
    b = ilist()
    si = []
    gr = {}
    for j in range(n):
        if a[j] == b[j]:
            si.append(j)
        else:
            k = (min(a[j], b[j]), max(a[j], b[j]))
            gr.setdefault(k, []).append(j)
    if n % 2 == 0:
        if si:
            print("-1")
            return
    else:
        if len(si) != 1:
            print("-1")
            return
    ok = True
    for k in gr:
        if len(gr[k]) != 2:
            ok = False
            break
    if not ok:
        print("-1")
        return
    tar = [None]*n
    hal = n // 2
    sp = [(j, n-1-j) for j in range(hal)]
    gl = list(gr.values())
    gl.sort(key=lambda x: x[0])
    if len(gl) != hal:
        print("-1")
        return
    for (l, r), (j1, j2) in zip(sp, gl):
        if a[j1] == b[j2] and a[j2] == b[j1]:
            tar[l] = j1
            tar[r] = j2
        elif a[j2] == b[j1] and a[j1] == b[j2]:
            tar[l] = j2
            tar[r] = j1
        else:
            ok = False
            break
    if not ok:
        print("-1")
        return
    if n % 2:
        mid = n // 2
        tar[mid] = si[0]
    cur = list(range(n))
    op = []
    pos = [0]*n
    for j in range(n):
        pos[cur[j]] = j
    for j in range(n):
        if cur[j] != tar[j]:
            k = pos[tar[j]]
            cur[j], cur[k] = cur[k], cur[j]
            pos[cur[j]] = j
            pos[cur[k]] = k
            op.append((j+1, k+1))
    print(len(op))
    for x, y in op:
        print(x, y)

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

