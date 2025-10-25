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
    n = ipt()
    grid = [list(input()), list(input()), list(input())]
    q = ipt()
    base = [[ [INF]*3 for _ in range(3) ] for __ in range(64)]
    for mask in range(64):
        d = [[INF]*6 for _ in range(6)]
        for u in range(6):
            if (mask >> u) & 1:
                d[u][u] = 0
        for u, v in ((0,1),(1,2),(3,4),(4,5),(0,3),(1,4),(2,5)):
            if ((mask >> u) & 1) and ((mask >> v) & 1):
                d[u][v] = 1
                d[v][u] = 1
        for k in range(6):
            if ((mask >> k) & 1) == 0: 
                continue
            for i in range(6):
                if ((mask >> i) & 1) == 0: continue
                di, aik = d[i], d[i][k]
                if aik >= INF: continue
                s0 = aik + d[k][0];  s1 = aik + d[k][1];  s2 = aik + d[k][2]
                s3 = aik + d[k][3];  s4 = aik + d[k][4];  s5 = aik + d[k][5]
                if s0 < di[0]: di[0] = s0
                if s1 < di[1]: di[1] = s1
                if s2 < di[2]: di[2] = s2
                if s3 < di[3]: di[3] = s3
                if s4 < di[4]: di[4] = s4
                if s5 < di[5]: di[5] = s5
        for i in range(3):
            if ((mask >> i) & 1) == 0: 
                continue
            base[mask][i][0] = d[i][3]
            base[mask][i][1] = d[i][4]
            base[mask][i][2] = d[i][5]

    data = []
    for c in range(n - 1):
        mask = 0
        if grid[0][c] == '.': mask |= 1 << 0
        if grid[1][c] == '.': mask |= 1 << 1
        if grid[2][c] == '.': mask |= 1 << 2
        if grid[0][c + 1] == '.': mask |= 1 << 3
        if grid[1][c + 1] == '.': mask |= 1 << 4
        if grid[2][c + 1] == '.': mask |= 1 << 5
        data.append(base[mask])

    temp = [[0 if i == j else INF for j in range(3)] for i in range(3)]




    st = SegmentTree(data, default=temp)

    res = []
    for _ in range(q):
        r, c = ivars()
        r -= 1; c -= 1
        grid[r][c] = '.' if grid[r][c] == '#' else '#'
        if 0 <= c - 1 < n - 1:
            pos = c - 1
            mask = 0
            if grid[0][pos] == '.': mask |= 1 << 0
            if grid[1][pos] == '.': mask |= 1 << 1
            if grid[2][pos] == '.': mask |= 1 << 2
            if grid[0][pos + 1] == '.': mask |= 1 << 3
            if grid[1][pos + 1] == '.': mask |= 1 << 4
            if grid[2][pos + 1] == '.': mask |= 1 << 5
            st[pos] = base[mask]
        if 0 <= c < n - 1:
            pos = c
            mask = 0
            if grid[0][pos] == '.': mask |= 1 << 0
            if grid[1][pos] == '.': mask |= 1 << 1
            if grid[2][pos] == '.': mask |= 1 << 2
            if grid[0][pos + 1] == '.': mask |= 1 << 3
            if grid[1][pos + 1] == '.': mask |= 1 << 4
            if grid[2][pos + 1] == '.': mask |= 1 << 5
            st[pos] = base[mask]
        root = st.data[1]
        res.append(-1 if root[0][2] >= INF else root[0][2])

    print(ljoin(res))



#================================================

class SegmentTree:
    def __init__(self, data, default=0, func=lambda A, B: [[min(A[i][0] + B[0][j], A[i][1] + B[1][j], A[i][2] + B[2][j]) for j in range(3)] for i in range(3)]):
        """initialize the segment tree with data"""
        self._default = default
        self._func = func
        self._len = len(data)
        self._size = _size = 1 << (self._len - 1).bit_length()

        self.data = [default] * (2 * _size)
        self.data[_size:_size + self._len] = data
        for i in reversed(range(_size)):
            self.data[i] = func(self.data[i + i], self.data[i + i + 1])

    def __delitem__(self, idx):
        self[idx] = self._default

    def __getitem__(self, idx):
        return self.data[idx + self._size]

    def __setitem__(self, idx, value):
        idx += self._size
        self.data[idx] = value
        idx >>= 1
        while idx:
            self.data[idx] = self._func(self.data[2 * idx], self.data[2 * idx + 1])
            idx >>= 1

    def __len__(self):
        return self._len

    def query(self, start, stop):
        """func of data[start, stop)"""
        start += self._size
        stop += self._size

        res_left = res_right = self._default
        while start < stop:
            if start & 1:
                res_left = self._func(res_left, self.data[start])
                start += 1
            if stop & 1:
                stop -= 1
                res_right = self._func(self.data[stop], res_right)
            start >>= 1
            stop >>= 1

        return self._func(res_left, res_right)

    def __repr__(self):
        return "SegmentTree({0})".format(self.data)

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

