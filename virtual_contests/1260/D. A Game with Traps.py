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
    m, n, k, t = ivars()
    a = ilist()
    arr = []
    for _ in range(k):
        l, r, d = ivars()
        arr.append((l, r + 1, d))
    def cond(x):
        new = []
        for l, r, d in arr:
            if d > x:
                new.append((l, r))
        s = segmentUnionLength(new)
        return n + 1 + 2 * s <= t
    def binsearch(low, high, condition):
        result = None
        while low <= high:
            mid = (low + high) // 2
            if condition(mid):
                result = mid
                high = mid - 1
            else:
                low = mid + 1
        return result
    mx = binsearch(0, 2*(10**5) + 1, cond)
    if mx == None:
        print(0)
    res = 0
    for i in a:
        if i >= mx:
            res += 1
    print(res)

#================================================
def segmentUnionLength(segments):

    # Size of given segments list
    n = len(segments)
    if n == 0: return 0

    # Initialize empty points container
    points = [None] * (n * 2)

    # Create a vector to store starting
    # and ending points
    for i in range(n):
        points[i * 2] = (segments[i][0], False)
        points[i * 2 + 1] = (segments[i][1], True)

    # Sorting all points by point value
    points = sorted(points, key=lambda x: x[0])

    # Initialize result as 0
    result = 0

    # To keep track of counts of current open segments
    # (Starting point is processed, but ending point
    # is not)
    Counter = 0

    # Traverse through all points
    for i in range(0, n * 2):

        # If there are open points, then we add the
        # difference between previous and current point.
        if (i > 0) & (points[i][0] > points[i - 1][0]) &  (Counter > 0):
            result += (points[i][0] - points[i - 1][0])

        # If this is an ending point, reduce, count of
        # open points.
        if points[i][1]:
            Counter -= 1
        else:
            Counter += 1
    return result
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

