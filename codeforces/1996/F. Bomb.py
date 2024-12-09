import sys, math
from collections import deque, defaultdict, Counter

MOD       = 10**9 + 7
FASTIO    = True
DEBUG     = False
INF       = float('inf')
NINF      = float('-inf')
YES, NO   = "YES", "NO"
MT        = True

#====================Solution====================
def calculate_score(a, b, k, cutoff):
    score = 0
    operations = 0
    remaining = []

    for ai, bi in zip(a, b):
        if ai >= cutoff:
            cycles = min((ai - cutoff + bi - 1) // bi, k - operations)
            score += (2 * ai - (cycles - 1) * bi) * cycles // 2
            operations += cycles
            if operations == k:
                return score
            remaining_value = ai - cycles * bi
            if remaining_value > 0:
                remaining.append(remaining_value)
        elif ai > 0:
            remaining.append(ai)

    remaining.sort(reverse=True)
    return score + sum(remaining[:k - operations])

def ternary_search(a, b, k):
    left, right = 0, max(a) + 1

    for _ in range(100):
        m1 = left + (right - left) // 3
        m2 = right - (right - left) // 3

        f1 = calculate_score(a, b, k, m1)
        f2 = calculate_score(a, b, k, m2)

        if f1 < f2:
            left = m1
        else:
            right = m2

    return max(calculate_score(a, b, k, left), calculate_score(a, b, k, right))

def solve(n, k, a, b):
    total_operations = sum((ai - 1) // bi + 1 for ai, bi in zip(a, b))
    if k >= total_operations:
        return sum(ai * (ai // bi + 1) - bi * (ai // bi) * (ai // bi + 1) // 2 for ai, bi in zip(a, b))
    return ternary_search(a, b, k)

def sol():
    n, k = ivars()
    a = ilist()
    b = ilist()
    print(solve(n, k, a, b))
    return
    def cond(low, k):
        res = 0
        for i in range(n):
            if a[i] < low: continue
            steps = min((a[i] - low)//b[i] + 1, k)
            k -= steps
            res += steps * a[i] - b[i] * (steps - 1)
    def bs(lo, hi, condition):
        while lo < hi:
            mid = (lo + hi) // 2
            if condition(mid, k):
                hi = mid
            else:
                lo = mid + 1
        return lo
    low = bs(1, max(a) + 1, cond)
    res = 0
    for i in range(n):
        if a[i] < low: continue
        steps = min((a[i] - low)//b[i] + 1, k)
        k -= steps
        res += steps * a[i] - b[i] * (steps - 1)
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

