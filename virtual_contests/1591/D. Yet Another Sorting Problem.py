import sys, math
from collections import deque, defaultdict, Counter
import operator

MOD       = 10**9 + 7
INF       = float('inf')
NINF      = float('-inf')
YES, NO   = "YES", "NO"
MT        = True
OUT       = []
#---------------------------------------------------
def sol():
    n = ipt()
    a = ilist()
    seen = set()
    for i in a:
        if str(i) in seen:
            OUT.append(YES)
            return
        seen.add(str(i))
    #st = SegmentTree(n+1, neutral = 0, func = operator.add)
    st = FenwickTree(n+1)
    inversions = 0
    for i in range(n):
        inversions += st.query_range(a[i], n + 1)
        st.update(a[i], 1)

    OUT.append(NO if inversions & 1 else YES)




#---------------------------------------------------

class FenwickTree:
    def __init__(self, size):
        self.n = size
        self.tree = [0] * (size + 1)

    def update(self, index, value):
        while index <= self.n:
            self.tree[index] += value
            index += index & (-index)

    def query(self, index):
        sum = 0
        while index > 0:
            sum += self.tree[index]
            index -= index & (-index)
        return sum

    def query_range(self, left, right):
        return self.query(right) - self.query(left - 1)

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

def main():
    for _ in range(ipt() if MT else 1): sol()
    print(njoin(OUT))

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


