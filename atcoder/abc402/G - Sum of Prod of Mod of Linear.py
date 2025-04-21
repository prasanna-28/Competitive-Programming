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
    N, M, A, B1, B2 = ivars()

    if A % M == 0:  
        print(str(N * (B1 % M) * (B2 % M)))
        return

    g = math.gcd(A, M)
    a = A // g
    m = M // g
    step = a % m or m
    if step <= m // 2:                
        H, inc_sign = step, 1
    else:
        H, inc_sign = m - step, -1

    inv = pow(step, -1, m)
    d = (H * inv) % m or m
    inc_val = inc_sign * g * H

    D = (B2 - B1) % M
    threshold = M - D
    total = 0

    for r in range(d):
        cnt = (N - 1 - r) // d + 1
        if cnt <= 0:
            continue
        X = (A * r + B1) % M
        left = cnt

        while left:
            if inc_val > 0:
                seg = min(left, (M - X + inc_val - 1) // inc_val)
                nb = 0 if X >= threshold else min(seg, (threshold - X + inc_val - 1) // inc_val)
            else:
                step = -inc_val
                seg = min(left, (X // step) + 1)
                nb = 0 if X < threshold else min(seg, (X - threshold) // step + 1)

            na = seg - nb
            if nb:
                sumX = nb * X + inc_val * nb * (nb - 1) // 2
                sumX2 = (
                    nb * X * X
                    + 2 * X * inc_val * nb * (nb - 1) // 2
                    + inc_val * inc_val * (nb - 1) * nb * (2 * nb - 1) // 6
                )
                total += sumX2 + D * sumX
            if na:
                start = X + inc_val * nb
                sumX = na * start + inc_val * na * (na - 1) // 2
                sumX2 = (
                    na * start * start
                    + 2 * start * inc_val * na * (na - 1) // 2
                    + inc_val * inc_val * (na - 1) * na * (2 * na - 1) // 6
                )
                total += sumX2 + (D - M) * sumX

            left -= seg
            X = (X + inc_val * seg) % M

    print(total)
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

