import sys, math
from collections import deque, defaultdict, Counter

MOD       = 10**9 + 7
FASTIO    = False
DEBUG     = False
INF       = float('inf')
NINF      = float('-inf')
YES, NO   = "YES", "NO"
MT        = False

#====================Solution====================
def sol():
    n, c = ivars()
    apps = [ilist() + [i+1] for i in range(n)]
    g2 = []
    g1 = []
    for a in apps:
        d, s, _ = a
        if d > s:
            g2.append(a)
        else:
            g1.append(a)

    g2.sort(key=lambda x: x[0]-x[1], reverse=True)
    m = len(g2)

    dp = [[-1]*(m+1) for _ in range(m+1)]
    ch = [[0]*(m+1) for _ in range(m+1)]
    dp[0][0] = c
    for i in range(1, m+1):
        d, s, _ = g2[i-1]
        for j in range(i+1):
            if dp[i-1][j] > dp[i][j]:
                dp[i][j] = dp[i-1][j]
                ch[i][j] = 0
            if j > 0 and dp[i-1][j-1] != -1 and dp[i-1][j-1] >= d:
                cand = dp[i-1][j-1] - s
                if cand > dp[i][j]:
                    dp[i][j] = cand
                    ch[i][j] = 1

    g1.sort(key=lambda x: x[1])
    best_total = -1
    best_j = -1
    best_rem = -1
    for j in range(m+1):
        if dp[m][j] != -1:
            rem = dp[m][j]
            safe_count = 0
            tmp = rem
            for a in g1:
                d, s, _ = a
                if tmp >= s:
                    safe_count += 1
                    tmp -= s
            total = j + safe_count
            if total > best_total:
                best_total = total
                best_j = j
                best_rem = dp[m][j]

    cg2 = []
    i = m
    j = best_j
    while i:
        if j and ch[i][j] == 1:
            cg2.append(g2[i-1])
            j -= 1
        i -= 1
    cg2.reverse()

    cg1 = []
    R = best_rem
    for a in g1:
        d, s, _ = a
        if R >= s:
            cg1.append(a)
            R -= s

    ans = [x[2] for x in cg2] + [x[2] for x in cg1]
    tot = len(ans)
    print(tot)
    print(ljoin(ans))



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

