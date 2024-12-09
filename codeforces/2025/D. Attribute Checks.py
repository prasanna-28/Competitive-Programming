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
    n, m = ivars()
    r = ilist()
    zeros_positions = [i for i in range(n) if r[i] == 0]
    t = [0] * (m + 2)
    t[0] = -1
    for i in range(m):
        t[i + 1] = zeros_positions[i]
    t[m + 1] = n

    pass_count = [{} for _ in range(m + 1)]
    for k in range(m + 1):
        start = t[k] + 1
        end = t[k + 1]
        events = r[start:end]
        for s in range(0, k + 1):
            intell = k - s
            count = 0
            for ri in events:
                if ri > 0:
                    if intell >= ri:
                        count += 1
                elif ri < 0:
                    if s >= -ri:
                        count += 1
            pass_count[k][s] = count

    dp = [{} for _ in range(m + 1)]
    dp[0][0] = 0
    for k in range(m):
        for s in dp[k]:
            current_passed = dp[k][s]
            s_new = s + 1
            if s_new <= k + 1:
                int_new = (k + 1) - s_new
                new_passed = current_passed + pass_count[k + 1].get(s_new, 0)
                if s_new in dp[k + 1]:
                    dp[k + 1][s_new] = max(dp[k + 1][s_new], new_passed)
                else:
                    dp[k + 1][s_new] = new_passed
            s_new = s
            int_new = (k + 1) - s_new
            new_passed = current_passed + pass_count[k + 1].get(s_new, 0)
            if s_new in dp[k + 1]:
                dp[k + 1][s_new] = max(dp[k + 1][s_new], new_passed)
            else:
                dp[k + 1][s_new] = new_passed

    max_passed = 0
    for s in dp[m]:
        max_passed = max(max_passed, dp[m][s])

    print(max_passed)

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

