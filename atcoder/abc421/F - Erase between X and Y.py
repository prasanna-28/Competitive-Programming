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
    q = ipt()
    queries = []
    need = []
    for idx in range(q):
        idx += 1
        i = input()
        if i[0] == '1':
            x = int(i.split(' ')[1])
            queries.append((idx, x))
            need.append((idx, x))
        else:
            x = i.split(' ')[1:]
            a = int(x[0])
            b = int(x[1])
            queries.append((idx, a, b))
    linked = [[0, -1]]
    idxmap = {0:0}
    for new, prev in need:
        previdx = idxmap[prev]
        prevnode = linked[previdx]
        newnode = [new, prevnode[1]]
        prevnode[1] = len(linked)
        idxmap[new] = len(linked)
        linked.append(newnode)
    idxes = {}
    i = 0
    node = 0
    while node != -1:
        val, next = linked[node]
        idxes[val] = i
        i += 1
        node = next
    seg = LazySegmentTree([0] * (i + 1))
    for i in queries:
        if len(i) == 2:
            # print(i)
            new, prev = i
            seg[idxes[new]] = new
            # track[idxes[new]] = new
        else:
            _, l, r = i
            left = idxes[l]
            right = idxes[r]
            left, right = min(left, right) + 1, max(left, right)
            #print(l, r)
            #print(track)
            print(seg.range_sum(left, right))
            seg.range_zero(left, right)





#================================================
class LazySegmentTree:
    def __init__(self, data):
        self._len = len(data)
        self._size = size = 1 << (self._len - 1).bit_length()
        self.data = [0] * (2 * size)
        self._lz0 = [False] * (2 * size)
        self.data[size:size + self._len] = data
        for i in range(size - 1, 0, -1):
            self.data[i] = self.data[i << 1] + self.data[i << 1 | 1]

    def __len__(self):
        return self._len

    def _apply_zero(self, idx):
        self.data[idx] = 0
        self._lz0[idx] = True

    def _push(self, idx):
        if self._lz0[idx]:
            lc = idx << 1
            rc = lc | 1
            self._apply_zero(lc)
            self._apply_zero(rc)
            self._lz0[idx] = False

    def _update(self, idx):
        for h in range(idx.bit_length() - 1, 0, -1):
            self._push(idx >> h)

    def _build(self, idx):
        idx >>= 1
        while idx:
            if self._lz0[idx]:
                self.data[idx] = 0
            else:
                self.data[idx] = self.data[idx << 1] + self.data[idx << 1 | 1]
            idx >>= 1

    def range_zero(self, l, r):
        l0 = l + self._size
        r0 = r + self._size
        L, R = l0, r0
        while l0 < r0:
            if l0 & 1:
                self._apply_zero(l0)
                l0 += 1
            if r0 & 1:
                r0 -= 1
                self._apply_zero(r0)
            l0 >>= 1
            r0 >>= 1
        self._update(L)
        self._build(L)
        self._update(R - 1)
        self._build(R - 1)

    def range_sum(self, l, r):
        l += self._size
        r += self._size
        self._update(l)
        self._update(r - 1)
        res = 0
        while l < r:
            if l & 1:
                res += self.data[l]
                l += 1
            if r & 1:
                r -= 1
                res += self.data[r]
            l >>= 1
            r >>= 1
        return res

    def __setitem__(self, idx, value):
        i = idx + self._size
        self._update(i)
        self.data[i] = value
        self._lz0[i] = False
        self._build(i)

    def __repr__(self):
        return f"LazySegmentTree({self.data})"
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

