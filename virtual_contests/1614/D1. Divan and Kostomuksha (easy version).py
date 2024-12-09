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
    n = int(input())
    a = list(map(int, input().split()))

    MAX_VAL = max(a) + 1

    # Count occurrences of each number
    cnt = [0] * MAX_VAL
    for x in a:
        cnt[x] += 1

    # Compute divisors for each number
    divisors = [[] for _ in range(MAX_VAL)]
    for i in range(1, MAX_VAL):
        for j in range(i, MAX_VAL, i):
            divisors[j].append(i)

    # Initialize dp array
    dp = [0] * MAX_VAL

    # Compute dp
    for x in range(MAX_VAL - 1, 0, -1):
        if cnt[x] == 0:
            continue
        current_sum = x * cnt[x]
        for d in divisors[x]:
            if d == x:
                dp[d] = max(dp[d], current_sum)
            else:
                dp[d] = max(dp[d], dp[x] + d * (cnt[d] - cnt[x]))

    # Find the maximum value in dp
    print(max(dp))

def __sol():
    n = int(input())
    a = list(map(int, input().split()))

    MAX_VAL = 5000001

    cnt = [0] * MAX_VAL
    for x in a:
        cnt[x] += 1

    dp = [0] * MAX_VAL
    for i in range(1, MAX_VAL):
        dp[i] = i * cnt[i]

    for x in range(MAX_VAL - 1, 0, -1):
        if dp[x] == 0:
            continue
        i = 2
        while i * i <= x:
            if x % i == 0:
                dp[x // i] = max(dp[x // i], dp[x] + (cnt[x // i] - cnt[x]) * (x // i))
                if i * i != x:
                    dp[x // (x // i)] = max(dp[x // (x // i)], dp[x] + (cnt[x // (x // i)] - cnt[x]) * (x // (x // i)))
            i += 1

    print(max(dp))


def _sol():
    n = ipt()
    arr = ilist()
    arr.sort(reverse=True)  # Sort in descending order

    max_val = arr[0]
    factor_count = defaultdict(int)
    result = 0

    def get_factors(num):
        factors = set()
        for i in range(1, int(num**0.5) + 1):
            if num % i == 0:
                factors.add(i)
                factors.add(num // i)
        return sorted(factors, reverse=True)

    for num in arr:
        factors = get_factors(num)
        for factor in factors:
            if factor_count[factor] == 0:
                result += factor
                for subfactor in get_factors(factor):
                    factor_count[subfactor] += 1
                break

    print(result)

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

