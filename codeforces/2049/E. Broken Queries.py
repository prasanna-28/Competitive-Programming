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
def query(l, r):
    print('?', l, r, flush = True)
    return ipt()

def answer(x):
    print('!', x, flush = True)

def sol():
    n = ipt()
    curr_interval = (1, n)
    c1, c2 = curr_interval
    diff = (c2 - c1 + 1)//4
    l1 = c1 + diff
    l2 = l1 + diff
    l3 = l2 + diff
    q1 = query(c1, l1 - 1)
    q2 = query(l1, l2 - 1)
    q3 = query(l2, l3 - 1)
    a = sorted([q1, q2, q3])
    if a == [0, 1, 1]:
        q4 = 1
    if a == [0, 0, 1]:
        q4 = 0
    if a == [1, 1, 1]:
        q4 = 0
    if a == [0, 0, 0]:
        q4 = 1
    a.append(q4)
    a.sort()
    low = 2
    high = n - 1
    k_bigger = a == [0, 0, 0, 1]
    if k_bigger: first_contains = q1 == 1 or q2 == 1
    else: first_contains = q1 == 0 or q2 == 0

    if first_contains: t1, t2 = query(1, n//2), 0
    else: t1, t2 = query(n//2 + 1, n), n//2

    if t1:
        high = n//2
        while low < high:
            mid = (low + high) // 2
            if not query(t2 + 1, t2 + mid): low = mid + 1
            else: high = mid
        answer(low)
        return
    low = n//2 + 1
    if not t2:
        while low < high:
            mid = (low + high) // 2
            if query(n - mid + 1, n): low = mid + 1
            else: high = mid
        answer(low)
        return
    while low < high:
        mid = (low + high) // 2
        if query(1, mid): low = mid + 1
        else: high = mid
    answer(low)

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

