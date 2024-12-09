import sys, math
from collections import deque, defaultdict, Counter

MOD       = 10**9 + 7
INF       = float('inf')
NINF      = float('-inf')
YES, NO   = "YES", "NO"
MT        = True


def query(t, i, j, x):
    print('?', t, i, j, x, flush = True)
    u = int(input())
    if u == -1: exit(1)
    return u

def answer(p):
    print("!", ljoin(p), flush = True)
#---------------------------------------------------
def sol():
    n = ipt()
    if n == 3:
        res = [0] * 4
        i,j,k = 1,2,3
        a1 = query(2, i, j, 2)
        a2 = query(2, j, i, 2)
        a3 = query(2, k, i, 2)
        if a1 == 3:
            res[i] = 3
        elif a2 == 3:
            res[j] = 3
        else:
            res[k] = 3
        a1 = query(2, i, j, 1)
        a2 = query(2, j, i, 1)
        a3 = query(2, k, j, 1)
        if a1 == 1:
            res[i] = 1
        elif a2 == 1:
            res[j] = 1
        else:
            res[k] = 1
        for i in range(1, 4):
            if res[i] == 0:
                res[i] = 2
                break
        answer(res[1:])
        return
    res = [0] * (n + 1)
    for i in range(1, n, 2):
        j = i + 1
        a1 = query(1, i, j, n-1)
        a2 = query(2, i, j, 1)
        # one is i, j is a1 and the other is a2
        a3 = min(a1, a2)
        a4 = query(2, i, j, a3)
        if a4 == a3:
            ires = min(a1, a2)
            jres = max(a1, a2)
        else:
            ires = max(a1, a2)
            jres = min(a1, a2)
        res[i] = ires
        res[j] = jres
    _2 = []
    _3 = []
    for i,v in enumerate(res):
        if v == 2:
            _2.append(i)
        if v == n-1:
            _3.append(i)
    if len(_2) > 1:
        i = _2[0]
        j = _2[1]
        a1 = query(2, i, j, 1)
        if a1 == 1:
            res[i] = 1
            res[j] = 2
        else:
            res[j] = 1
            res[i] = 2
    if len(_3) > 1:
        i = _3[0]
        j = _3[1]
        a1 = query(2, i, j, n - 1)
        if a1 == n - 1:
            res[i] = n - 1
            res[j] = n
        else:
            res[j] = n - 1
            res[i] = n
    if n & 1:
        seen = [False] * (n+1)
        for i in res:
            seen[i] = True
        for j in range(1, n+1):
            if not seen[j]:
                res[-1] = j
                break
    answer(res[1:])



#---------------------------------------------------
'''

t=1
: max(min(x,pi),min(x+1,pj))
;
t=2
: min(max(x,pi),max(x+1,pj))
.

i j k

max(min(1, i), min(2, j))
min(max(2, i), max(2, j))
max(min(1, j), min(2, i))

min(max(2, j), max(3, i))
min(max(2, j), max(3, i))

min(max(1, i), max(2, j))
min(max(1, i), max(2, j))

'''



def main():
    for _ in range(ipt() if MT else 1): sol()

# import os
# from io import BytesIO, IOBase
#
# _str = str
# str = lambda x=b"": x if type(x) is bytes else _str(x).encode()
#
# BUFSIZE = 8192
#
#
# class FastIO(IOBase):
#     newlines = 0
#
#     def __init__(self, file):
#         self._file = file
#         self._fd = file.fileno()
#         self.buffer = BytesIO()
#         self.writable = "x" in file.mode or "r" not in file.mode
#         self.write = self.buffer.write if self.writable else None
#
#     def read(self):
#         while True:
#             b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
#             if not b:
#                 break
#             ptr = self.buffer.tell()
#             self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
#         self.newlines = 0
#         return self.buffer.read()
#
#     def readline(self):
#         while self.newlines == 0:
#             b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
#             self.newlines = b.count(b"\n") + (not b)
#             ptr = self.buffer.tell()
#             self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
#         self.newlines -= 1
#         return self.buffer.readline()
#
#     def flush(self):
#         if self.writable:
#             os.write(self._fd, self.buffer.getvalue())
#             self.buffer.truncate(0), self.buffer.seek(0)
#
#
# class IOWrapper(IOBase):
#     def __init__(self, file):
#         self.buffer = FastIO(file)
#         self.flush = self.buffer.flush
#         self.writable = self.buffer.writable
#         self.write = lambda s: self.buffer.write(s.encode("ascii"))
#         self.read = lambda: self.buffer.read().decode("ascii")
#         self.readline = lambda: self.buffer.readline().decode("ascii")
#
#
# sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
# input = lambda: sys.stdin.readline().rstrip("\r\n")

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

