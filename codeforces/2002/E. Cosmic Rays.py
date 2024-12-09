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
    n = ipt()
    pairs = [ivars() for _ in range(n)]
    dp = {}
    times = []
    currmax = 0
    maxval = -1
    currs = 0

    for ai, bi in pairs:
        if ai > currmax:
            currmax = ai
            maxval = bi
            dp.clear()
            dp[bi] = (currmax, 0)
            currs = 0
        else:
            if bi not in dp:
                dp[bi] = (ai, currs)
            else:
                prev, last = dp[bi]
                new_val = prev + ai - (currs - last)
                dp[bi] = (max(new_val, ai), currs)

            if dp[bi][0] > currmax:
                currmax = dp[bi][0]
                maxval = bi
                new_dp = {bi: (currmax, 0)}
                dp = new_dp
                currs = 0
            elif dp[bi][0] == currmax and bi != maxval:
                maxval = bi
                new_dp = {bi: (currmax, 0)}
                dp = new_dp
                currs = 0

        currs = max(currs, ai)
        times.append(currmax)

    print(ljoin(times))



#================================================
# dp[bi] = ai - diff(last, prev) + times[-1]
# what is the maximum length whcih can be achieved?
# res = max(maximum length + time to achieve) over all maxlens
# how long does it take for the previous bi to make it to current?
# is the current and previous maxlens big enough?
# the new maxlen is the combination of these twos after they connect.
# res does nto change unless this new maxlen + time to achieve is big enough
# res only changes if the current value is a new maxlen or combines with previous maxlen
# only maxlen can combine, nothing else can
#
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

