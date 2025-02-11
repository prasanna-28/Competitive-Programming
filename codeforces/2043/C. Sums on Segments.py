import sys, math
from collections import deque, defaultdict, Counter

MOD       = 10**9 + 7
FASTIO    = False
DEBUG     = False
INF       = float('inf')
NINF      = float('-inf')
YES, NO   = "YES", "NO"
MT        = True

#====================Solution====================
def sol():
    n = ipt()
    arr = ilist()
    x_pos = -1
    for i, val in enumerate(arr):
        if val != 1 and val != -1:
            x_pos = i
            break

    if x_pos == -1:
        min_sub, max_sub, _ = min_max_subarray_sum(arr)

        intervals = []
        intervals.append([min_sub, max_sub])

        if 0 < min_sub or 0 > max_sub:
            intervals.append([0, 0])

        merged = merge_intervals(intervals)
        all_vals = expand_intervals(merged)
        print(str(len(all_vals)))
        print(" ".join(map(str, all_vals)))
        return

    x_val = arr[x_pos]
    left_part = arr[:x_pos]
    right_part = arr[x_pos+1:]

    Lmin, Lmax, pL = min_max_subarray_sum(left_part)
    Rmin, Rmax, pR = min_max_subarray_sum(right_part)


    Lsuf_min, Lsuf_max = (0, 0)
    if len(left_part) > 0:
        Lsuf_min, Lsuf_max = suffix_range(pL)

    Rpref_min, Rpref_max = (0, 0)
    if len(right_part) > 0:
        Rpref_min, Rpref_max = prefix_range(pR)

    intervals = []

    intervals.append([Lmin, Lmax])
    intervals.append([Rmin, Rmax])


    cross_min = x_val + (Lsuf_min + Rpref_min)
    cross_max = x_val + (Lsuf_max + Rpref_max)
    intervals.append([cross_min, cross_max])

    intervals.append([0, 0])

    merged = merge_intervals(intervals)
    all_vals = expand_intervals(merged)

    print(str(len(all_vals)))
    print(" ".join(map(str, all_vals)))


#================================================

def prefix_sums(arr):

    p = [0] * (len(arr)+1)
    for i in range(len(arr)):
        p[i+1] = p[i] + arr[i]
    return p

def min_max_subarray_sum(arr):

    p = prefix_sums(arr)


    min_pref = 0
    max_pref = 0
    min_sub = 0
    max_sub = 0

    for j in range(1, len(p)):
        candidate_max = p[j] - min_pref
        if candidate_max > max_sub:
            max_sub = candidate_max

        candidate_min = p[j] - max_pref
        if candidate_min < min_sub:
            min_sub = candidate_min

        if p[j] < min_pref:
            min_pref = p[j]
        if p[j] > max_pref:
            max_pref = p[j]

    return min_sub, max_sub, p

def suffix_range(p):

    total = p[-1]

    min_p = min(p)
    max_p = max(p)
    return total - max_p, total - min_p

def prefix_range(p):

    return min(p), max(p)

def merge_intervals(intervals):

    intervals.sort(key=lambda x: x[0])
    merged = []
    for st, en in intervals:
        if not merged:
            merged.append([st, en])
        else:
            if st <= merged[-1][1] + 1:
                merged[-1][1] = max(merged[-1][1], en)
            else:
                merged.append([st, en])
    return merged

def expand_intervals(intervals):

    out = []
    for st, en in intervals:
        out.extend(range(st, en+1))
    return out

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

