import sys, math
from collections import deque, defaultdict, Counter

MOD       = 998244353
FASTIO    = True
DEBUG     = False
INF       = float('inf')
NINF      = float('-inf')
YES, NO   = "YES", "NO"
MT        = True

#====================Solution====================
max_f = 5 * 10**5
fct = [1] * (max_f + 1)
for i in range(1, max_f + 1):
    fct[i] = fct[i-1] * i % MOD
inv_f = [1] * (max_f + 1)
inv_f[max_f] = pow(fct[max_f], MOD-2, MOD)
for i in range(max_f - 1, -1, -1):
    inv_f[i] = inv_f[i+1] * (i+1) % MOD
def sol():
    c = ilist()
    s_t = sum(c)
    E = (s_t + 1) // 2
    O = s_t // 2
    
    vld = True
    for num in c:
        if num > E and num > O:
            vld = False
            break
    if not vld:
        print(0)
        return
    
    m_in = []
    m_no = []
    opt = []
    s_in = 0
    s_no = 0
    s_op = 0
    
    for num in c:
        if num == 0:
            continue
        if num <= E and num > O:
            m_in.append(num)
            s_in += num
        elif num > E and num <= O:
            m_no.append(num)
            s_no += num
        else:
            opt.append(num)
            s_op += num
    
    if s_in > E or s_no > O:
        print(0)
        return
    
    req = E - s_in
    if req < 0:
        print(0)
        return
    
    if s_op < req:
        print(0)
        return
    
    dp = [0] * (req + 1)
    dp[0] = 1
    for num in opt:
        for i in range(req, num - 1, -1):
            dp[i] = (dp[i] + dp[i - num]) % MOD
    
    cnt = dp[req]
    
    p_f = 1
    for num in c:
        p_f = p_f * fct[num] % MOD
    
    ans = fct[E] * fct[O] % MOD
    ans = ans * pow(p_f, MOD-2, MOD) % MOD
    ans = ans * cnt % MOD
    print(ans)
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

