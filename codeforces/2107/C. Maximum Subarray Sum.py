import sys, math
from collections import deque, defaultdict, Counter

MOD       = 10**9 + 7
FASTIO    = False
DEBUG     = False
INF       = float('inf')
NINF      = float('-inf')
YES, NO   = "YES", "NO"
MT        = True

def mcss(a):
    ms=cs=a[0]
    for x in a[1:]:
        cs = x if cs<0 else cs+x
        if cs>ms: ms=cs
    return ms

#====================Solution====================
def sol():
    n, k = ivars()
    s = input()
    a = ilist()
    i = 0
    while i < len(s):
        curr = []
        while i < len(s) and s[i] == '1':
            curr.append(a[i])
            i += 1
        if len(curr) != 0:
            if mcss(curr) > k:
                print(NO)
                return
        else:
            i += 1
    
    if '0' not in s:
        if mcss(a) != k:
            print(NO)
            return
    else:
        i = 0
        while s[i] != '0':
            i += 1
        c = i
        i += 1
        while i < len(s):
            if s[i] == '0':
                a[i] = -pow(10, 18)
            i += 1
        left = c - 1
        right = c + 1
        l = []
        r = []
        while left >= 0 and s[left] == '1':
            l.append(a[left])
            left -= 1
        while right < len(a) and s[right] == '1':
            r.append(a[right])
            right += 1
        p = [0]
        for i in l:
            p.append(p[-1] + i)
        p2 = [0]
        for i in r:
            p2.append(p2[-1] + i)
        m1 = max(p)
        m2 = max(p2)
        a[c] = (k - m1 - m2)
    print(YES)
    print(ljoin(a))

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

