import sys, math
from collections import deque, defaultdict, Counter

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
    who = [0]*(q+1)
    is_plus = [False]*(q+1)
    for t in range(1, q+1):
        si, c = input().split()
        si = int(si)
        who[t] = si
        is_plus[t] = (c == '+')

    E = [[0]*(q+1) for _ in range(n)]
    S = [[0]*(q+1) for _ in range(n)]

    for t in range(1, q+1):
        for i in range(n):
            E[i][t] = E[i][t-1]
            S[i][t] = S[i][t-1]
        snake_id = who[t] - 1
        if is_plus[t]:
            E[snake_id][t] = E[snake_id][t-1] + 1
        else:
            S[snake_id][t] = S[snake_id][t-1] + 1

    MxE = [max(E[i]) for i in range(n)]

    D = [[0]*n for _ in range(n)]

    for i in range(n):
        Ei = E[i]
        for j in range(n):
            Sj = S[j]
            best = -10**15
            for t in range(q+1):
                diff = Ei[t] - Sj[t]
                if diff > best:
                    best = diff
            D[i][j] = best + 1

    INF = 10**18
    dp_maxC = [[INF]*n for _ in range(1<<n)]
    dp_offset = [[0]*n for _ in range(1<<n)]

    for i in range(n):
        mask = (1 << i)
        dp_maxC[mask][i] = 1 + MxE[i]
        dp_offset[mask][i] = 0

    full_mask = (1 << n) - 1

    for mask in range(1<<n):
        m_val = dp_maxC[mask]
        o_val = dp_offset[mask]

        for last in range(n):
            if not (mask & (1<<last)):
                continue
            currMaxC = m_val[last]
            if currMaxC == INF:
                continue
            currOffset = o_val[last]

            others = full_mask ^ mask
            s = others
            while s:
                lowbit = s & -s
                j = (lowbit).bit_length() - 1

                s ^= lowbit

                dist = D[last][j]
                newOffset = currOffset + dist
                newMaxC = max(currMaxC, 1 + newOffset + MxE[j])

                newMask = mask | (1<<j)
                if newMaxC < dp_maxC[newMask][j]:
                    dp_maxC[newMask][j] = newMaxC
                    dp_offset[newMask][j] = newOffset
                elif newMaxC == dp_maxC[newMask][j]:
                    if newOffset < dp_offset[newMask][j]:
                        dp_offset[newMask][j] = newOffset

    ans = min(dp_maxC[full_mask])
    print(ans)


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

