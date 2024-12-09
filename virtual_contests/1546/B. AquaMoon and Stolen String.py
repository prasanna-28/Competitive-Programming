import sys, math
from collections import deque, defaultdict, Counter

MOD       = 10**9 + 7
FASTIO    = not True
DEBUG     = False
INF       = float('inf')
NINF      = float('-inf')
YES, NO   = "YES", "NO"
MT        = True

#====================Solution====================
def sol():
    n, m = ivars()
    original = [input() for _ in range(n)]
    strings = [input() for _ in range(n-1)]
    trie = [[0, [-1] * 26]]
    def insert(word):
        node = 0
        i = 0
        while i < m:
            if ~trie[node][1][ord(word[i]) - 97]:
                node = trie[node][1][ord(word[i]) - 97]
            else:
                trie[node][1][ord(word[i]) - 97] = len(trie)
                trie.append([0, [-1] * 26])
            i += 1
        trie[node][0] = 1
    for i in original:
        insert(i)
    node = 0
    word = []
    for i in range(m):
        cts = [0] * 26
        for j in range(n):
            cts[ord(original[j][i]) - 97] += 1
        for j in range(n - 1):
            cts[ord(strings[j][i]) - 97] -= 1
        for i in range(len(cts)):
            if cts[i]:
                word.append(chr(i + 97))
                node = trie[node][1][i]
                break
    print(''.join(word))

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

