import sys, math
from collections import deque, defaultdict, Counter

MOD       = 10**9 + 7
FASTIO    = True
DEBUG     = False
INF       = float('inf')
NINF      = float('-inf')
YES, NO   = "YES", "NO"
MT        = False

def sieve(n):
    """
    Returns a list of all prime numbers up to n using the Sieve of Eratosthenes algorithm.

    Parameters:
    n (int): The upper limit of numbers to check for primality.

    Returns:
    List[int]: A list containing all prime numbers up to n.
    """
    if n < 2:
        return []

    is_prime = [True] * (n + 1)
    is_prime[0], is_prime[1] = False, False

    for p in range(2, int(n**0.5) + 1):
        if is_prime[p]:
            for multiple in range(p*p, n + 1, p):
                is_prime[multiple] = False

    primes = [num for num, prime in enumerate(is_prime) if prime]
    return primes

primes = sieve(pow(10, 6) + 5)

#====================Solution====================
def sol():
    n = ipt()
    a = ilist()
    map = defaultdict(int)
    k = 0
    for i in a:
        factors = []
        uppr = math.isqrt(i) + 5
        for prime in primes:
            if prime > uppr:
                break
            if i % prime == 0:
                factors.append(prime)
                while i % prime == 0:
                    i//=prime
        if i != 1:
            factors.append(i)
        s = 0
        print(factors)
        for factor in factors:
            s += map[factor]
            s %= MOD
        if k == 0:
            s = 1
        if k == n - 1:
            print(s)
            return
        k += 1
        for factor in factors:
            map[factor] += s
            map[factor] %= MOD


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

