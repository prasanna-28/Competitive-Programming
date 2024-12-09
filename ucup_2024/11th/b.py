
import sys, math
from collections import deque, defaultdict, Counter

MOD       = 998_244_353
FASTIO    = False
DEBUG     = False
INF       = float('inf')
NINF      = float('-inf')
YES, NO   = "YES", "NO"
MT        = False


fact = [1]
inv = [1]

for i in range(1, 3001):
    fact.append(fact[-1] * i % MOD)
    inv.append(pow(fact[-1], -1, MOD))

comb = lambda x, y: (x>=y) * fact[x] * inv[x - y] % MOD * inv[y] % MOD

#====================Solution====================
def sol():
    n, m = ivars()
    arr = sorted(ilist())
    dp = []
    for _ in range(n + 1):
        dp.append([0] * (m + 1))
    dp[0][0] = 1
    arr.reverse()
    res = [0] * (n + 1)
    for i in range(n):
        total = 0
        for j in range(m + 1):
            layer = min(m, arr[i] + j)
            if dp[i][j]:
                dp[i + 1][layer] = (dp[i + 1][layer] + dp[i][j]) % MOD
                dp[i + 1][j] = (dp[i + 1][j] + dp[i][j]) % MOD
                if arr[i] + j + 1 > m: total = (total + dp[i][j]) % MOD
        for k in range(n + 1):
            res[k] = (res[k] + total * comb(n - i - 1, k)) % MOD

    print('\n'.join(map(str, res)))

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

