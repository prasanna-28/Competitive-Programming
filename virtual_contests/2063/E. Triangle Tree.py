import sys, math
from collections import deque, defaultdict, Counter

MOD       = 10**9 + 7
FASTIO    = True
DEBUG     = False
INF       = float('inf')
NINF      = float('-inf')
YES, NO   = "YES", "NO"
MT        = True

def nC2(x):
    return x*(x-1)//2

#====================Solution====================
def sol():
    n = ipt()

    graph = [[] for _ in range(n+1)]
    for _ in range(n-1):
        u, v = ivars()
        graph[u].append(v)
        graph[v].append(u)

    if n == 1:
        print(0)
        return

    depth = [0]*(n+1)
    subtree_size = [0]*(n+1)
    children = [[] for _ in range(n+1)]
    parent = [-1] * (n + 1)

    dfs(1, parent, graph, depth, subtree_size, children)

    A = sum(depth[1:])

    L = 0
    for x in range(1, n+1):
        s_x = subtree_size[x]
        if s_x <= 1:
            continue
        pairs_subtree_x = nC2(s_x)
        for c in children[x]:
            s_c = subtree_size[c]
            if s_c >= 2:
                pairs_subtree_x -= nC2(s_c)
        L += depth[x] * pairs_subtree_x

    dvals = depth[1:]
    dvals.sort()

    ps = [0]*(n+1)
    for i in range(1, n+1):
        ps[i] = ps[i-1] + dvals[i-1]

    M = 0

    for v in range(2, n+1):
        M += ps[v-1]

    pairs_count = nC2(n)
    H = 2*M - 2*L - pairs_count
    ans = H + A
    print(ans)

#================================================


def dfs(root, parent, graph, depth, subtree_size, children):

    stack = [(root, -1, False)]

    while stack:
        node, par, returning = stack.pop()

        if not returning:
            if par != -1:
                depth[node] = depth[par] + 1
                children[par].append(node)

            stack.append((node, par, True))

            for w in graph[node]:
                if w == par:
                    continue
                parent[w] = node
                stack.append((w, node, False))

        else:
            subtree_size[node] = 1
            for c in children[node]:
                subtree_size[node] += subtree_size[c]


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

