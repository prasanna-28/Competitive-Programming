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
    a = input()
    b = input()
    blockA = []
    blockB = []
    i = 0
    while i < len(a):
        if a[i] == '0':
            size = 0
            while i < len(a) and a[i] == '0' and i < len(a):
                i += 1
                size += 1
            blockA.append([0, size])
        else:
            size = 0
            while i < len(a) and a[i] == '1' and i < len(a):
                i += 1
                size += 1
            blockA.append([1, size])
    i = 0
    while i < len(b):
        if b[i] == '0':
            size = 0
            while i < len(b) and  b[i] == '0':
                i += 1
                size += 1
            blockB.append([0, size])
        else:
            size = 0
            while i < len(b) and b[i] == '1':
                i += 1
                size += 1
            blockB.append([1, size])
    # want to make A -> B
    blockB.reverse()
    blockA.reverse()
    haveA = []
    ops = 0
    if blockB[-1][0] != blockA[-1][0]:
        blockA.append((blockB[-1][0], 0))
    while len(blockA):
        curr, size = blockA.pop()
        while len(blockA) and blockA[-1][0] == curr:
            size += blockA.pop()[1]
        if len(blockB) == 0: break
        targetSize = blockB.pop()[1]
        while size < targetSize:
            if len(blockA) < 2:
                break
            before = blockA[-2][1]
            last, current_size = blockA.pop()
            if len(blockA) >= 2:
                blockA[-2][1] += current_size
            else:
                blockA = [[last, current_size]] + blockA
            size += before
            blockA.pop()
            ops += 1
        if size == targetSize:
            haveA.append([curr, size])
        else:
            print(-1)
            return
    res = []
    for c, s in haveA:
        for _ in range(s):
            res.append(c)
    res = ''.join(map(str, res))
    if res == b:
        print(ops)
    else:
        print(-1)


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

