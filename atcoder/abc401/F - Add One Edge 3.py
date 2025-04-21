import sys, math
from collections import deque, defaultdict, Counter

MOD       = 10**9 + 7
FASTIO    = False
DEBUG     = False
INF       = float('inf')
NINF      = float('-inf')
YES, NO   = "YES", "NO"
MT        = not True

#====================Solution====================
def sol():
    
    
    n1 = ipt()
    
    adj1 = [[] for _ in range(n1 )]
    for _ in range(n1 - 1):
        u, v = ivars()
        u -= 1
        v -= 1
        adj1[u].append(v)
        adj1[v].append(u)


    
    n2 = ipt()
    adj2 = [[] for _ in range(n2 )] 
    for _ in range(n2 -1 ):
        u, v = ivars()
        adj2[u - 1].append(v - 1)
        adj2[v - 1].append(u - 1)


    dists1 = [-1] * (n1 )
    dists2 = [-1] * (n2 )
 
    q = deque([(0, 0)])
    seen = set([0])
    while q:
        curr, d = q.popleft()
        dists1[curr] = max(dists1[curr], d)
        for node in adj1[curr]:
            if node in seen: continue
            seen.add(node)
            q.append((node, d + 1))

    mx = max(range(n1 ), key = lambda x: dists1[x])
    q = deque([(mx, 0)])
    seen = set([mx])
    while q:
        curr, d = q.popleft()
        dists1[curr] = max(dists1[curr], d)
        for node in adj1[curr]:
            if node in seen: continue
            seen.add(node)
            q.append((node, d + 1))

    mx = max(range(n1 ), key = lambda x: dists1[x])
    q = deque([(mx, 0)])
    seen = set([mx])
    while q:
        curr, d = q.popleft()
        dists1[curr] = max(dists1[curr], d)
        for node in adj1[curr]:
            if node in seen: continue
            seen.add(node)
            q.append((node, d + 1))


    q = deque([(0, 0)])
    seen = set([0])
    while q:
        curr, d = q.popleft()
        dists2[curr] = max(dists2[curr], d)
        for node in adj2[curr]:
            if node in seen: continue
            seen.add(node)
            q.append((node, d + 1))

    mx = max(range(n2 ), key = lambda x: dists2[x])
    q = deque([(mx, 0)])
    seen = set([mx])
    while q:
        curr, d = q.popleft()
        dists2[curr] = max(dists2[curr], d)
        for node in adj2[curr]:
            if node in seen: continue
            seen.add(node)
            q.append((node, d + 1))

    mx = max(range(n2 ), key = lambda x: dists2[x])
    q = deque([(mx, 0)])
    seen = set([mx])
    while q:
        curr, d = q.popleft()
        dists2[curr] = max(dists2[curr], d)
        for node in adj2[curr]:
            if node in seen: continue
            seen.add(node)
            q.append((node, d + 1))
    d1 = max(dists1)
    d2 = max(dists2)
    d = max(d1, d2)
    d1 = sorted(dists1)
    d2 = sorted(dists2)
    amount = 0
    from bisect import bisect_left
    for i in d1:
        amount += bisect_left(d2, d - i + 1)
    res = amount * d + (n1 * n2 - amount)
    for i in dists1:
        res += (n2) * i
    for i in dists2:
        res += (n1) * i

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

