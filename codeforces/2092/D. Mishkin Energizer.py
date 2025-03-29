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
    n = ipt()
    s = input()
    L, I, T = 0,0,0
    for i in s:
        if i == 'L':
            L += 1
        if i == 'I':
            I += 1
        if i == 'T':
            T += 1
    if L == I == T:
        print(0)
        return
    if max(L, I, T) == n:
        print(-1)
        return
    arr = [(L, 'L'), (T, 'T'), (I, 'I')]
    arr.sort(key = lambda x: x[0])
    new = []
    for i in s:
        if i == arr[0][1]:
            new.append('L')
        elif i == arr[1][1]:
            new.append('T')
        else:
            new.append('I')
    # L is smallest, T is next smallest, I is the biggest
    order = [i[0] for i in arr]
    diff = order[1] - order[0]
    ops = []
    for i in range(n - 1, 0, -1):
        if new[i] != new[i - 1] and new[i] == 'I':
            while order[0] != order[2]:
                ops.append(i)
                i += 1
                ops.append(i)
                i += 1
                order[0] += 1
                order[1] += 1
            break
        elif new[i] != new[i - 1] and new[i - 1] == 'I':
            while order[0] != order[2]:
                ops.append(i)
                ops.append(i)
                order[0] += 1
                order[1] += 1
            break
    
    newnew = new[::]
    for l in ops:
        left = newnew[l - 1]
        right = newnew[l]
        k = ['L', 'T', 'I']
        for i in k:
            if i != left and i != right:
                newnew.insert(l, i)

    for i in range(len(newnew) - 1, 0, -1):
        if newnew[i] != newnew[i - 1] and newnew[i - 1] == 'T':
            while order[0] != order[1]:
                ops.append(i)
                ops.append(i)
                order[0] += 1
                order[2] += 1
            break
        elif newnew[i] != newnew[i - 1] and newnew[i] == 'T':
            while order[0] != order[1]:
                ops.append(i)
                i += 1
                ops.append(i)
                i += 1
                order[0] += 1
                order[2] += 1
            break
    if order[0] == order[1] == order[2]:
        print(len(ops))
        for i in ops:
            print(i)
    else:
        print(-1)


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

