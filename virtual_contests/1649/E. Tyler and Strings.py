import sys
import math
import operator
from collections import deque, defaultdict, Counter, OrderedDict
from functools import cache, partial, reduce
from itertools import *

MOD       = 998244353
INF       = float('inf')
NINF      = float('-inf')
YES,NO    = "YES", "NO"
DEBUG     = 0
CONTRACTS = 1
MT        = 0
OUT       = []

factorial = [1]
for i in range(1, 200_005):
    factorial.append((factorial[-1] * i) % MOD)

#---------------------------------------------------
def sol():
    n, m = ivars()
    s = ilist()
    t = ilist()
    c = Counter(s)
    arr = [0] * (200_005)
    for i in c.keys():
        arr[i] = c[i]
    st = SegmentTree(arr)
    res = 0
    entire = factorial[n]
    for i in c:
        entire *= pow(factorial[c[i]], -1, MOD)
        entire %= MOD
    for i in range(min(len(s), len(t))):
        curr = t[i]
        under = st.query(0, curr)
        res += under * (entire * pow(n, -1, MOD))
        res %= MOD
        if st[curr]:
            entire *= pow(n, -1, MOD)
            n -= 1
            entire *= st[curr]
            st[curr] -= 1
            entire %= MOD
        else:
            break
    else:
        if len(t) > len(s):
            res += 1
    print(res % MOD)



def combine(a, b):
    return a + b

class SegmentTree:
    def __init__(self, data, default=0, func=combine):
        """initialize the segment tree with data"""
        self._default = default
        self._func = func
        self._len = len(data)
        self._size = _size = 1 << (self._len - 1).bit_length()

        self.data = [default] * (2 * _size)
        self.data[_size:_size + self._len] = data
        for i in reversed(range(_size)):
            self.data[i] = func(self.data[i + i], self.data[i + i + 1])

    def __delitem__(self, idx):
        self[idx] = self._default

    def __getitem__(self, idx):
        return self.data[idx + self._size]

    def __setitem__(self, idx, value):
        idx += self._size
        self.data[idx] = value
        idx >>= 1
        while idx:
            self.data[idx] = self._func(self.data[2 * idx], self.data[2 * idx + 1])
            idx >>= 1

    def __len__(self):
        return self._len

    def query(self, start, stop):
        """func of data[start, stop)"""
        start += self._size
        stop += self._size

        res_left = res_right = self._default
        while start < stop:
            if start & 1:
                res_left = self._func(res_left, self.data[start])
                start += 1
            if stop & 1:
                stop -= 1
                res_right = self._func(self.data[stop], res_right)
            start >>= 1
            stop >>= 1

        return self._func(res_left, res_right)

    def __repr__(self):
        return "SegmentTree({0})".format(self.data)


#---------------------------------------------------
def main():
    if MT:
        for _ in range(ipt()):
            sol()
    else:
        sol()

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

