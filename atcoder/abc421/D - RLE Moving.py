import sys, math
from collections import deque, defaultdict, Counter

MOD       = 10**9 + 7
FASTIO    = False
DEBUG     = False
INF       = float('inf')
NINF      = float('-inf')
YES, NO   = "YES", "NO"
MT        = not True

#====================Solution====================
def sol():
    rt, ct, ra, ca = ivars()
    n, m, l = ivars()
    s,t = [],[]
    for _ in range(m):
        si, ai = input().split()
        s.append((si, int(ai)))
    for _ in range(l):
        ti, bi = input().split()
        t.append((ti, int(bi)))
    sx, sy, tx, ty = rt, ct, ra, ca
    i = j = 0
    newS, newT = [], []
    rs = s[0][1] if s else 0
    rtlen = t[0][1] if t else 0
    while i < len(s) and j < len(t):
        take = rs if rs < rtlen else rtlen
        newS.append((s[i][0], take))
        newT.append((t[j][0], take))
        rs -= take
        rtlen -= take
        if rs == 0:
            i += 1
            if i < len(s):
                rs = s[i][1]
        if rtlen == 0:
            j += 1
            if j < len(t):
                rtlen = t[j][1]
    res = 0
    for i in range(len(newS)):
        dS, steps = newS[i]
        dT, _ = newT[i]
        diffx = sx - tx
        diffy = sy - ty
        if dS == 'U':
            vsx, vsy = -1, 0
        elif dS == 'D':
            vsx, vsy = 1, 0
        elif dS == 'L':
            vsx, vsy = 0, -1
        else:
            vsx, vsy = 0, 1
        if dT == 'U':
            vtx, vty = -1, 0
        elif dT == 'D':
            vtx, vty = 1, 0
        elif dT == 'L':
            vtx, vty = 0, -1
        else:
            vtx, vty = 0, 1
        dx = vsx - vtx
        dy = vsy - vty
        if dx == 0 and dy == 0:
            if diffx == 0 and diffy == 0:
                res += steps
        elif dx == 0:
            if diffx == 0 and dy != 0 and (-diffy) % dy == 0:
                k = (-diffy) // dy
                if 1 <= k <= steps:
                    res += 1
        elif dy == 0:
            if diffy == 0 and dx != 0 and (-diffx) % dx == 0:
                k = (-diffx) // dx
                if 1 <= k <= steps:
                    res += 1
        else:
            if (-diffx) % dx == 0 and (-diffy) % dy == 0:
                kx = (-diffx) // dx
                ky = (-diffy) // dy
                if kx == ky and 1 <= kx <= steps:
                    res += 1
        sx += vsx * steps
        sy += vsy * steps
        tx += vtx * steps
        ty += vty * steps
    print(res)




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

