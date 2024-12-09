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
    n, k, w, h = map(int, input().split())
    s = input()

    def simulate(initial_vert, initial_hor):
        vert, hor = initial_vert, initial_hor
        pos = [0, 0]
        count = 0
        for i in s:
            if pos == [0, 0]:
                count += 1
            if i == 'U':
                if vert == 1:
                    if pos[1] + 1 <= h:
                        pos[1] += 1
                    else:
                        vert *= -1
                        pos[1] -= 1
                else:
                    if pos[1] - 1 >= 0:
                        pos[1] -= 1
                    else:
                        vert *= -1
                        pos[1] += 1
            elif i == 'D':
                if vert == 1:
                    if pos[1] - 1 >= 0:
                        pos[1] -= 1
                    else:
                        vert *= -1
                        pos[1] += 1
                else:
                    if pos[1] + 1 <= h:
                        pos[1] += 1
                    else:
                        vert *= -1
                        pos[1] -= 1
            elif i == 'L':
                if hor == 1:
                    if pos[0] - 1 >= 0:
                        pos[0] -= 1
                    else:
                        hor *= -1
                        pos[0] += 1
                else:
                    if pos[0] + 1 <= w:
                        pos[0] += 1
                    else:
                        hor *= -1
                        pos[0] -= 1
            elif i == 'R':
                if hor == 1:
                    if pos[0] + 1 <= w:
                        pos[0] += 1
                    else:
                        hor *= -1
                        pos[0] -= 1
                else:
                    if pos[0] - 1 >= 0:
                        pos[0] -= 1
                    else:
                        hor *= -1
                        pos[0] += 1
        if pos == [0, 0]:
            count += 1
        return count, vert, hor

    # Simulate for all initial orientations
    results = {
        (1, 1): simulate(1, 1),
        (-1, 1): simulate(-1, 1),
        (1, -1): simulate(1, -1),
        (-1, -1): simulate(-1, -1)
    }

    total_count = 0
    curr_vert, curr_hor = 1, 1

    for _ in range(k):
        count, next_vert, next_hor = results[(curr_vert, curr_hor)]
        total_count += count
        curr_vert, curr_hor = next_vert, next_hor

    print(total_count)



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

