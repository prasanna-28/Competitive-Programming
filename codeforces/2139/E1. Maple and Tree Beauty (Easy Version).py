import sys, math
from collections import deque, defaultdict, Counter

MOD       = 10**9 + 7
FASTIO    = False
DEBUG     = False
INF       = float('inf')
NINF      = float('-inf')
YES, NO   = "YES", "NO"
MT        = True

# subset sum code with logorithmic decomposition
def subset_sum_reachability(nums, k):
    mask = (1 << (k + 1)) - 1
    dp = 1
    cnt = Counter(nums)
    for v, c in cnt.items():
        if v <= 0:
            continue
        c = min(c, k // v)
        t = 1
        while c > 0:
            s = min(t, c)
            dp = dp | ((dp << (v * s)) & mask)
            c -= s
            t <<= 1
    return [bool((dp >> i) & 1) for i in range(k + 1)]

def reachable(nums, k):
    reach = subset_sum_reachability(nums, k)
    return [i for i in range(k + 1) if reach[i]]
#====================Solution====================
def sol():
    n, k = ivars()
    p = ilist()
    adj = [[] for _ in range(n + 1)]
    for i,v in enumerate(p):
        adj[v].append(i + 2)
    a, b = min(n - k, n), max(n - k, k)
    layersizes = [1]
    prev = [1]
    while True:
        layer = []
        for node in prev:
            layer += adj[node]
            if len(adj[node]) == 0:
                break
        else:
            layersizes.append(len(layer))
            prev = layer
            continue
        break
    np = n - sum(layersizes)
    a = reachable(layersizes, k)
    for i in a:
        if k - np <= i:
            print(len(layersizes))
            break
    else:
        print(len(layersizes) - 1)

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

