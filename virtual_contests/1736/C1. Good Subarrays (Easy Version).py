import sys, math
from collections import deque, defaultdict, Counter

MOD       = 10**9 + 7
INF       = float('inf')
NINF      = float('-inf')
YES, NO   = "YES", "NO"
MT        = True

#---------------------------------------------------
def sol():
    n = ipt()
    a = ilist()
    res = 0
    i = 0
    l = 0
    curr = 1
    while i < n:
        while i < n and a[i] >= curr:
            i += 1
            l += 1
            res += l
            curr += 1
        l = a[i] - 1 if i < n else INF
        curr = a[i] if i < n else INF
    print(res)



#---------------------------------------------------
def main():
    for _ in range(ipt() if MT else 1): sol()

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
