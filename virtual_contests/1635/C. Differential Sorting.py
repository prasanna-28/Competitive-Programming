import sys
import math
import operator
from collections import deque, defaultdict, Counter, OrderedDict
from functools import cache, partial, reduce
from itertools import *

MOD       = 10**9 + 7
INF       = float('inf')
NINF      = float('-inf')
YES,NO    = "YES", "NO"
DEBUG     = 0
CONTRACTS = 1
MT        = 1
OUT       = []

#---------------------------------------------------
def sol():
    n = ipt()
    a = ilist()
    if a[-1] < 0:
        print(-1 if a != list(sorted(a)) else 0)
        return
    if a[-2] > a[-1]:
        print(-1)
        return
    print(n-2)
    for i in range(n-2):
        print(i+1, n-2+1, n-1+1)

#---------------------------------------------------
def main():
    if MT:
        for _ in range(ipt()):
            sol()
    else:
        sol()

class SegmentTree:
    def __init__(self, length, neutral = INF, func = min):
        self._size = 1
        self._neutral = neutral
        while self._size < length: self._size <<= 1
        self.arr = [self._neutral]*(self._size*2)
        self._func = func

    def __setitem__(self, idx, value):
        self._set(idx, value, 0, 0, self._size)

    def __delitem__(self, idx):
        self[idx] = self._neutral

    def __getitem__(self, idx):
        return self.query(idx, idx + 1)

    def __len__(self):
        return len(self.arr)

    def __repr__(self):
        res = []
        x = 1
        l = 0
        while l < len(self.arr):
            curr = []
            for _ in range(x):
                curr.append(self.arr[l])
                l += 1
                if l >= len(self.arr): break
            else:
                res.append(ljoin(curr))
            x <<= 1
        return '\n'.join(res)

    def _op(self, a, b):
        return self._func(a,b)

    def _build(self, arr, x, lx, rx):
        if rx - lx == 1:
            if lx < len(arr):
                self.arr[x] = arr[lx]
            return
        m = (rx + lx)//2
        self._build( arr, 2*x + 1, lx, m)
        self._build( arr, 2*x + 2, m, rx)
        self.arr[x] = self._op(self.arr[2*x + 1], self.arr[2*x + 2])

    def build(self, arr):
        self._build(arr, 0, 0, self._size)

    def _set(self, i, v, x, lx, rx):
        if rx - lx <= 1:
            # leaf node
            self.arr[x] = v
            return

        m = (lx + rx) // 2
        if i < m:
            self._set(i, v, 2*x + 1, lx, m)
        else:
            self._set(i, v, 2*x + 2, m, rx)

        self.arr[x] = self._op(self.arr[2*x + 1], self.arr[2*x + 2])

    def _query(self, l, r, x, lx, rx):
        if lx >= r or l >= rx: return self._neutral
        if lx >= l and rx <= r: return self.arr[x]
        m = (lx + rx) // 2
        a1 = self._query(l, r, 2*x + 1, lx, m)
        a2 = self._query(l, r, 2*x + 2, m, rx)
        return self._op(a1, a2)

    def query(self, l, r):
        # l <= i < r
        return self._query(l, r, 0, 0, self._size)


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
    debug       = lambda **kwargs: (print("Dbg:"), print("\n".join([f"{key} = {value}" for key, value in kwargs.items()]))) if DEBUG else None
    main()
