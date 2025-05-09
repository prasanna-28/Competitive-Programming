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
def toposort(graph):
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

    # cycle check
    for node in res:
        if any(found[nei] for nei in graph[node]):
            return None
        found[node] = 0

    return res[::-1]

def sol():
    n = ipt()
    adj = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = ivars()
        adj[u-1].append(v-1)
        adj[v-1].append(u-1)
    ipt()
    primes = ilist()
    dag = [[] for _ in range(n)]
    q = deque([0])
    seen = [False] * n
    seen[0] = True
    while q:
        curr = q.popleft()
        for i in adj[curr]:
            if not seen[i]:
                dag[curr].append(i)
                q.append(i)
                seen[i] = True
    sizes = [0] * n
    prods = [0] * (n - 1)
    top = toposort(dag)
    assert(top != None)
    for i in range(len(top) - 1, -1, -1):
        node = top[i]
        size = 1
        for child in dag[node]:
            size += sizes[child]
        if node != 0:
            prods[node - 1] = (n - size) * size
        sizes[node] = size
    if len(primes) < n - 1:
        primes.extend([1] * (n - 1 - len(primes)))
    prods.sort()
    primes.sort()
    if len(primes) > n - 1:
        add = 1
        while len(primes) > n - 2:
            add *= primes.pop()
            add %= MOD
        primes.append(add)
    res = 0
    for i in range(n - 1):
        res += prods[i] * primes[i]
        res %= MOD
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

