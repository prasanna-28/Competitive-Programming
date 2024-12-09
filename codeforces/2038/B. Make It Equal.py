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
def binsearch(low, high, cond):
    """
    Finds the largest x in [low, high] such that cond(x) is True.

    :param low: Lower bound of search space (inclusive).
    :param high: Upper bound of search space (inclusive).
    :param cond: A function that takes an integer x and returns True or False.
    :return: The largest x for which cond(x) is True. Returns -1 if no such x exists.
    """
    result = -1  # Default if no x satisfies cond(x)
    while low <= high:
        mid = low + (high - low) // 2
        if cond(mid):
            result = mid  # Update result to the current mid
            low = mid + 1  # Try to find a larger x
        else:
            high = mid - 1  # Look for smaller x
    return result

def sol():
    n = ipt()
    arr = ilist()
    def cond(x):
        # @invariant cond(x) -> cond(x - 1) for all x > 0
        i = 0
        a = arr[:]
        s = sum(a)
        while s > (x * n):
            i = i % n
            if a[i] > x:
                sub = (a[i] - x + 1) // 2
                a[i] -= sub * 2
                a[(i + 1) % n] += sub
                s -= sub
            i += 1
        return all(i == x for i in a)

    x = binsearch(1, sum(arr)//n, cond)
    steps = 0
    if x == -1:
        print(-1)
        return
    i = 0
    a = arr[:]
    s = sum(a)
    while s > (x * n):
        i = i % n
        if a[i] > x:
            sub = (a[i] - x + 1) // 2
            a[i] -= sub * 2
            a[(i + 1) % n] += sub
            s -= sub
            steps += sub
        i += 1
    print(steps)


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

