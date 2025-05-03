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
    n = ipt()
    a = ilist()
    if n == 1:
        print(0)
        return
    trie = [[-1, -1, 0]]
    def insert(x):
        node = trie[0]
        node[2] += 1
        for i in map(int, bin(x)[2:].zfill(30)):
            if ~node[i]:
                node = trie[node[i]]
                node[2] += 1
            else:
                new = [-1, -1, 1]
                node[i] = len(trie)
                trie.append(new)
                node = new
    def remove(x):
        node = trie[0]
        node[2] -= 1
        for i in map(int, bin(x)[2:].zfill(30)):
            node = trie[node[i]]
            node[2] -= 1
    def query(x):
        node = trie[0]
        node2 = 0
        for i in map(int, bin(x)[2:].zfill(30)):
            node2 <<= 1
            if ~node[i] and trie[node[i]][2] != 0:
                node = trie[node[i]]
                node2 |= i
            else:
                node = trie[node[i ^ 1]]
                node2 |= (1^i)
        return x ^ node2, node2
    from heapq import heappush as hpush, heappop as hpop
    res = 0
    root = a.pop()
    for i in a:
        insert(i)
    tree = set([root])
    edge, node2 = query(root)
    h = [(edge, node2, root)]
    while len(tree) != n:
        mned, mnnod, prev = hpop(h)
        if mnnod in tree:
            edge, node2 = query(prev)
            hpush(h, (edge, node2, prev))
            continue
        res += mned
        remove(mnnod)
        tree.add(mnnod)
        if len(tree) == n: break
        edge, node2 = query(mnnod)
        hpush(h, (edge, node2, mnnod))
        edge, node2 = query(prev)
        hpush(h, (edge, node2, prev))
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

