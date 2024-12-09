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
    n, m, k = ivars()
    a = ilist()
    mx = max(a)
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u,v = ivars()
        adj[u-1].append(v-1)

    def cond(m):
        if m == -1: return True
        allowed_verts = set()
        for i in range(n):
            if a[i] <= m:
                allowed_verts.add(i)
        if len(allowed_verts) == 0:
            return False
        graph = [[] for _ in range(n)]
        for i in range(n):
            if i not in allowed_verts: continue
            for j in adj[i]:
                if j in allowed_verts:
                    graph[i].append(j)
        res, found = [], [0] * len(graph)
        stack = list(range(len(graph)))
        while stack:
            node = stack.pop()
            if node < 0:
                res.append(~node)
            elif not found[node]:
                found[node] = 1
                stack.append(~node)
                stack += graph[node]
        for node in res:
            if any(found[nei] for nei in graph[node]):
                return True
            found[node] = 0
        u = res[::-1]
        dp = [0] * n
        for i in range(len(u)-1, -1, -1):
            if u[i] not in allowed_verts: continue
            if not len(graph[i]):
                dp[i] = 1
                continue
            dp[i] = max(dp[j] for j in graph[i]) + 1
        return max(dp) >= k

    def binsearch(low, high, condition):
        while low < high:
            mid = low + (high - low) // 2
            if condition(mid):
                high = mid
            else:
                low = mid + 1
        return low

    res = binsearch(min(a), mx + 1, cond)
    print(res if res <= mx else -1)




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

