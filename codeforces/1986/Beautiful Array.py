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
    n, divisor = ivars()
    numbers = ilist()
    modCounts = defaultdict(lambda: defaultdict(int))
    for num in numbers:
        mod = str(num % divisor)
        modCounts[mod][str(num)] ^= 1

    oddCount = 0
    oddMod = '-1'
    for mod, counts in modCounts.items():
        if sum(counts.values()) % 2:
            oddCount += 1
            oddMod = mod

    if oddCount > 1:
        print(-1)
        return

    totalMoves = 0
    for mod, counts in modCounts.items():
        if mod == oddMod:
            continue
        nums = sorted(int(num) for num, count in counts.items() if count)
        for i in range(0, len(nums), 2):
            if i + 1 < len(nums):
                totalMoves += (nums[i+1] - nums[i]) // divisor

    if oddCount:
        nums = sorted(int(num) for num, count in modCounts[oddMod].items() if count)
        if len(nums) == 1:
            print(totalMoves)
            return

        prefixSum = [0] * len(nums)
        suffixSum = [0] * len(nums)

        for i in range(1, len(nums), 2):
            prefixSum[i] = nums[i] - nums[i-1]
            if i > 1:
                prefixSum[i] += prefixSum[i-2]

        for i in range(len(nums)-2, -1, -2):
            suffixSum[i] = nums[i+1] - nums[i]
            if i < len(nums) - 2:
                suffixSum[i] += suffixSum[i+2]

        minMoves = float('inf')
        for i in range(0, len(nums), 2):
            moves = 0
            if i > 0:
                moves += prefixSum[i-1]
            if i + 1 < len(nums):
                moves += suffixSum[i+1]
            minMoves = min(minMoves, moves)

        totalMoves += minMoves // divisor

    print(totalMoves)

def old_sol():
    n,k = ivars()
    a = ilist()
    a.sort(reverse = True)
    mods = defaultdict(list)
    ops = 0
    seen = False
    print(a)
    for v in a:
        mods[v % k].append(v)
    for i in mods:
        print(i, mods[i])
    for i in mods:
        curr = mods[i]
        if not len(curr) & 1:
            while len(curr) > 0:
                val = curr.pop()
                next = curr.pop()
                ops += (next - val)//k
        elif len(curr) & 1 and not seen:
            adder_1 = 0
            adder_2 = 0
            new = []
            seen = True
            print(curr)
            while len(curr) > 1:
                val = curr.pop()
                next = curr.pop()
                adder_1 += (next - val)//k
                new.append(val)
                new.append(next)
            new.append(curr.pop())
            print(new)
            while len(new) > 1:
                val = new.pop()
                next = new.pop()
                adder_2 += (val - next)//k
            print(adder_1, adder_2)
            ops += min(adder_1, adder_2)
        else:
            print(-1)
            return
    print(ops)

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

