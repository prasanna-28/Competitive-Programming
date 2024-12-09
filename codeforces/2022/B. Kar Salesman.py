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
def sol():
    line = ''
    while line.strip() == '':
        line = sys.stdin.readline()
    n = int(line.strip())
    s1 = ''
    while len(s1) < n:
        s1 += sys.stdin.readline().strip()
    s2 = ''
    while len(s2) < n:
        s2 += sys.stdin.readline().strip()
    # Precompute A's in each cell
    A1 = [1 if c == 'A' else 0 for c in s1]
    A2 = [1 if c == 'A' else 0 for c in s2]
    # Initialize DP
    dp_prev = [-1] * 3
    dp_prev[0] = 0
    for j in range(n):
        dp_next = [-1] *3
        for s in range(3):
            if dp_prev[s] == -1:
                continue
            if s ==0:
                if j+1 <n:
                    # Pattern 1: (0,j), (1,j), (0,j+1)
                    sum_A = A1[j] + A2[j] + A1[j+1]
                    vote = 1 if sum_A >=2 else 0
                    s_prime =2
                    if dp_next[s_prime] < dp_prev[s] + vote:
                        dp_next[s_prime] = dp_prev[s] + vote
                    # Pattern 2: (0,j), (1,j), (1,j+1)
                    sum_A = A1[j] + A2[j] + A2[j+1]
                    vote =1 if sum_A >=2 else 0
                    s_prime =1
                    if dp_next[s_prime] < dp_prev[s] + vote:
                        dp_next[s_prime] = dp_prev[s] + vote
                    # Pattern 3: (0,j), (0,j+1), (1,j+1)
                    sum_A = A1[j] + A1[j+1] + A2[j+1]
                    vote =1 if sum_A >=2 else 0
                    s_prime =0
                    if dp_next[s_prime] < dp_prev[s] + vote:
                        dp_next[s_prime] = dp_prev[s] + vote
                    # Pattern 4: (1,j), (0,j+1), (1,j+1)
                    sum_A = A2[j] + A1[j+1] + A2[j+1]
                    vote =1 if sum_A >=2 else 0
                    s_prime =0
                    if dp_next[s_prime] < dp_prev[s] + vote:
                        dp_next[s_prime] = dp_prev[s] + vote
            elif s ==1:
                if j+1 <n:
                    # Place district: (1,j), (0,j+1), (1,j+1)
                    sum_A = A2[j] + A1[j+1] + A2[j+1]
                    vote =1 if sum_A >=2 else 0
                    s_prime =0
                    if dp_next[s_prime] < dp_prev[s] + vote:
                        dp_next[s_prime] = dp_prev[s] + vote
            elif s ==2:
                if j+1 <n:
                    # Place district: (0,j), (0,j+1), (1,j+1)
                    sum_A = A1[j] + A1[j+1] + A2[j+1]
                    vote =1 if sum_A >=2 else 0
                    s_prime =0
                    if dp_next[s_prime] < dp_prev[s] + vote:
                        dp_next[s_prime] = dp_prev[s] + vote
        dp_prev = dp_next
    # After all columns, the residual state must be 0
    print(dp_prev[0] if dp_prev[0] != -1 else 0)

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

