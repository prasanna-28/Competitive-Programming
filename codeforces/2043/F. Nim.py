import sys, math
from collections import deque, defaultdict, Counter

MOD       = 998244353
MAXN = 100000
MAXA = 50
FASTIO    = True
DEBUG     = False
INF       = float('inf')
NINF      = float('-inf')
YES, NO   = "YES", "NO"
MT        = False

def comb2(n):
    return (n * (n-1) // 2) % MOD
pow2 = [1]*(MAXN+1)
for i in range(1, MAXN+1):
    pow2[i] = (pow2[i-1] * 2) % MOD
#====================Solution====================
def sol():
    n, q = ivars()
    a = ilist()
    pref = [[0]*(n+1) for _ in range(MAXA+1)]
    for i in range(n):
        val = a[i]
        for x in range(MAXA+1):
            pref[x][i+1] = pref[x][i]
        pref[val][i+1] += 1
    out = []
    def get_freq_array(L, R):
        length = R - L + 1
        f = [0]*(MAXA+1)
        for x in range(MAXA+1):
            f[x] = pref[x][R] - pref[x][L-1]
        return f
    for _ in range(q):
        L_, R_ = ivars()
        freq_arr = get_freq_array(L_, R_)
        m = R_ - L_ + 1

        ans = solve_subarray(freq_arr)
        if ans is None:
            out.append("-1")
        else:
            c, ways = ans
            out.append(f"{m - c} {ways % MOD}")

    print("\n".join(out))

def solve_subarray(freq):

    if freq[0] > 0:
        return (1, freq[0] % MOD)

    sum_pairs = 0
    for x in range(1, MAXA+1):
        if freq[x] >= 2:
            sum_pairs = (sum_pairs + comb2(freq[x])) % MOD
    if sum_pairs > 0:
        return (2, sum_pairs)

    L = []
    for x in range(1, MAXA+1):
        if freq[x] == 1:
            L.append(x)

    m = sum(freq)
    if len(L) == 0:
        return None

    basis = []
    for val in L:
        x = val
        for b in basis:
            x = min(x, x ^ b)
        if x != 0:
            basis.append(x)
    dim = len(basis)
    if dim == len(L):
        return None

    dp = [(INF, 0)] * 64

    for x in L:
        newdp = dp[:]

        old_card, old_ways = newdp[x]
        if 1 < old_card:
            newdp[x] = (1, 1)
        elif 1 == old_card:
            newdp[x] = (1, (old_ways + 1) % MOD)

        for s in range(64):
            (card_s, ways_s) = dp[s]
            if card_s == INF:
                continue
            new_s = s ^ x
            new_card = card_s + 1
            old_card, old_ways = newdp[new_s]
            if new_card < old_card:
                newdp[new_s] = (new_card, ways_s)
            elif new_card == old_card:
                newdp[new_s] = (old_card, (old_ways + ways_s) % MOD)

        dp = newdp

    best_c, best_w = dp[0]
    if best_c == INF:
        return None
    else:
        return (best_c, best_w % MOD)
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

