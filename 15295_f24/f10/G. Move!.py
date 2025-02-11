import sys, math
from collections import deque, defaultdict, Counter

MOD       = 10**9 + 7
FASTIO    = False
DEBUG     = False
INF       = float('inf')
NINF      = float('-inf')
YES, NO   = "YES", "NO"
MT        = False

#====================Solution====================
def sol():
    s = input()
    n = len(s)

    pairOf = [0] * (n - 1)
    base = ord('a')
    for i in range(n - 1):
        l  = ord(s[i])   - base
        r = ord(s[i+1]) - base
        pairOf[i] = l * 26 + r

    posOfPair = [[] for _ in range(26 * 26)]
    for i in range(n - 1):
        p = pairOf[i]
        posOfPair[p].append(i)


    m = ipt()
    visitedTime = [-1] * (n - 1)
    usedPairTime = [-1] * (26 * 26)
    dist = [0] * (n - 1)

    BFS_ID = 0
    out = []
    idx = 0
    for _ in range(m):
        f_, t_ = ivars()
        idx += 2

        start = f_ - 1
        goal  = t_ - 1

        if start == goal:
            out.append("0")
            continue

        BFS_ID += 1

        q = deque()
        q.append(start)
        visitedTime[start] = BFS_ID
        dist[start] = 0


        answer = None

        while q:
            cur = q.popleft()
            dcur = dist[cur]

            for nxt in (cur - 1, cur + 1):
                if 0 <= nxt < (n - 1):
                    if visitedTime[nxt] != BFS_ID:
                        visitedTime[nxt] = BFS_ID
                        dist[nxt] = dcur + 1
                        if nxt == goal:
                            answer = dist[nxt]
                            break
                        q.append(nxt)
            if answer is not None:
                break

            p = pairOf[cur]
            if usedPairTime[p] != BFS_ID:
                usedPairTime[p] = BFS_ID
                for nxt in posOfPair[p]:
                    if visitedTime[nxt] != BFS_ID:
                        visitedTime[nxt] = BFS_ID
                        dist[nxt] = dcur + 1
                        if nxt == goal:
                            answer = dist[nxt]
                            break
                        q.append(nxt)

                if answer is not None:
                    pass

            if answer is not None:
                break

        if answer is None:
            answer = dist[goal]

        out.append(str(answer))

    print("\n".join(out))

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

