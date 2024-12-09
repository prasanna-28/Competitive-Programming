import sys, math
from collections import deque, defaultdict, Counter
from bisect import bisect_left

MOD       = 10**9 + 7
FASTIO    = True
DEBUG     = False
INF       = float('inf')
NINF      = float('-inf')
YES, NO   = "YES", "NO"
MT        = False

#====================Solution====================
def sol():
    n, q = ivars()
    a = ilist()
    pref = [0]
    pref_2 = [0]
    idxes = defaultdict(list)
    idxes[0].append(0)
    x = 0
    for i in a:
        x += 1
        pref.append(pref[-1] ^ i)
        pref_2.append(pref_2[-1] + i)
        idxes[pref[-1]].append(x)
    for _ in range(q):
        l,r = ivars()
        if pref_2[r] == pref_2[l - 1]:
            print(0)
            continue
        if r - l + 1 <= 2:
            print(-1)
            continue
        if (r - l + 1) & 1:
            zero = pref[r] ^ pref[l - 1]
            if zero:
                print(2)
                continue
            print(1)
        else:
            zero = pref[l - 1] ^ pref[r]
            find = pref[l - 1]
            id = idxes[find]
            res = 4
            i1 = bisect_left(id, r)
            i2 = bisect_left(id, l - 1)
            for i in range(i1, i2, -1):
                if i >= len(id): continue
                i = id[i]
                if i == r: continue
                if not (r - i & 1) or (pref[i] != pref[l-1] and pref[i] != pref[r]):
                    continue
                if not zero:
                    if pref_2[i] == pref_2[r] or pref_2[i] == pref_2[l - 1]:
                        res = min(res, 1)
                    if r - i > 2 and i - l + 1 > 2:
                        res = min(res, 2)
                    else:
                        res = min(res, 3)
                else:
                    res = min(res, 3)

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

