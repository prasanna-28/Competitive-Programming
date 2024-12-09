
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
def handle_ccp(s, pos, seq, n):
    cnt, _, err = s
    if pos + 3 == n:
        err = True
        return cnt, pos + 1, err, True
    elif seq[pos + 3] == "C":
        cnt += 1
        pos += 1
    else:
        err = True
        pos += 1
    return cnt, pos, err, False

def handle_cpc(s, pos, seq, n):
    _, _, err = s
    if pos == 0:
        err = True
    elif seq[pos - 1] != "C":
        err = True
    pos += 1
    return s[0], pos, err, False

def handle_ccc(s, pos, seq, n):
    cnt, _, err = s
    if pos + 3 == n:
        err = True
        return cnt, pos + 1, err, True
    elif seq[pos + 3] == "C":
        err = True
        pos += 1
    else:
        if pos + 4 == n:
            err = True
            return cnt, pos + 1, err, True
        elif seq[pos + 4] == "C":
            pos += 1
        else:
            err = True
            pos += 1
    return cnt, pos, err, False

def sim(s, n, seq):
    cnt, pos, err = s
    while pos < n - 2:
        grp = seq[pos:pos+3]

        if grp == "CCP":
            cnt, pos, err, should_break = handle_ccp(s, pos, seq, n)
            s[0], s[2] = cnt, err
            if should_break:
                break

        elif grp == "CPC":
            cnt, pos, err, should_break = handle_cpc(s, pos, seq, n)
            s[0], s[2] = cnt, err
            if should_break:
                break

        elif grp == "CCC":
            cnt, pos, err, should_break = handle_ccc(s, pos, seq, n)
            s[0], s[2] = cnt, err
            if should_break:
                break

        else:
            pos += 1
    s[0], s[2] = cnt, err

def sol():
    n = int(input())
    seq = input()

    if n <= 3:
        print(1 if seq in {"CCC", "CCP", "CPC"} else 0)
        return

    s = [0, 0, False]
    sim(s, n, seq)
    print(s[0] + s[2])



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

