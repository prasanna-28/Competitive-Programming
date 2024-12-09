import sys, math
from collections import deque, defaultdict, Counter
sys.setrecursionlimit(2 * 10**5)

MOD       = 10**9 + 7
FASTIO    = True
DEBUG     = False
INF       = float('inf')
NINF      = float('-inf')
YES, NO   = "YES", "NO"
MT        = True

#====================Solution====================
def find_SCC(graph):
    SCC, S, P = [], [], []
    depth = [0] * len(graph)

    stack = list(range(len(graph)))
    while stack:
        node = stack.pop()
        if node < 0:
            d = depth[~node] - 1
            if P[-1] > d:
                SCC.append(S[d:])
                del S[d:], P[-1]
                for node in SCC[-1]:
                    depth[node] = -1
        elif depth[node] > 0:
            while P[-1] > depth[node]:
                P.pop()
        elif depth[node] == 0:
            S.append(node)
            P.append(len(S))
            depth[node] = len(S)
            stack.append(~node)
            stack += graph[node]
    return SCC[::-1]

def dfs(idx, adj, ht, par):
    global tim, mp

    if ht[idx] != -1:
        return ht[idx], 0

    tim += 1
    ht[idx] = tim

    res, tot = ht[idx], 1

    for val in adj[idx]:
        if val == par:
            continue
        low, cnt = dfs(val, adj, ht, idx)
        tot += cnt

        if low <= ht[idx]:
            res = min(res, low)
        else:
            mp[(idx, val)] = cnt

    ht[idx] = res
    return res, tot

def sol():
    n, m = map(int, input().split())
    adj = defaultdict(list)

    for _ in range(m):
        u, v = map(int, input().split())
        u, v = u - 1, v - 1
        adj[u].append(v)
        adj[v].append(u)

    low = [0] * n
    dis = [0] * n
    par = [-1] * n
    stk = []
    mp = {}
    cnt = [1] * n
    tim = 0

    stk.append((0, -1))
    while stk:
        idx, p = stk[-1]

        if dis[idx] == 0:
            tim += 1
            dis[idx] = low[idx] = tim

            for nxt in adj[idx]:
                if nxt != p:
                    if dis[nxt] == 0:
                        stk.append((nxt, idx))
                        par[nxt] = idx
        else:
            stk.pop()
            if p != -1:
                low[p] = min(low[p], low[idx])
                cnt[p] += cnt[idx]

                if low[idx] > dis[p]:
                    mp[(p, idx)] = cnt[idx]

    ans = n * (n - 1) // 2
    for val in mp.values():
        l, r = val, n - val
        ans = min(ans, (l * (l - 1) + r * (r - 1)) // 2)

    print(ans)


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

