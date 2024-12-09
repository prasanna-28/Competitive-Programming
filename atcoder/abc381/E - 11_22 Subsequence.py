import sys, math
from collections import deque, defaultdict, Counter

MOD       = 10**9 + 7
FASTIO    = True
DEBUG     = False
INF       = float('inf')
NINF      = float('-inf')
YES, NO   = "YES", "NO"
MT        = not True
from bisect import bisect_left, bisect_right
#====================Solution====================
def sol():
    n,q = ivars()
    s = input()
    idxes = []
    one_ct, two_ct = [0], [0]
    for i in range(n):
        if s[i] == '/':
            idxes.append(i)
        if s[i] == '1':
            one_ct.append(one_ct[-1] + 1)
        else:
            one_ct.append(one_ct[-1])
        if s[i] == '2':
            two_ct.append(two_ct[-1] + 1)
        else:
            two_ct.append(two_ct[-1])

    def get_ones(idx, left):
        return one_ct[idx] - one_ct[left]

    def get_twos(idx, right):
        return two_ct[right + 1] - two_ct[idx]

    for _ in range(q):
        l, r = ivars()
        l -= 1
        r -= 1
        il = bisect_left(idxes, l)
        ir = bisect_right(idxes, r) - 1
        if il >= len(idxes) or idxes[il] > r:
            print(0)
            continue
        if ir < 0 or idxes[ir] < l:
            print(0)
            continue
        res = max(min(get_ones(idxes[il], l), get_twos(idxes[il], r)), min(get_ones(idxes[ir], l), get_twos(idxes[ir], r)))
        while il <= ir:
            mid = (il + ir)//2
            one_count = get_ones(idxes[mid], l)
            two_count = get_twos(idxes[mid], r)
            if one_count > two_count:
                res = max(res, two_count)
                ir = mid - 1
            elif two_count > one_count:
                res = max(res, one_count)
                il = mid + 1
            else:
                res = one_count
                break
        print(res + res + 1)



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

