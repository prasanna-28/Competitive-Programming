
import   sys, math
finp   = sys.stdin.readline
MOD    = 10**9 + 7
njoin  = lambda x: '\n'.join(map(str, x))
ljoin  = lambda x: ' '.join(map(str, x))
sjoin  = lambda x: '\n'.join(x)
initl  = lambda x,y: [y]*x
INF    = float('inf')
NINF   = float('-inf')
ilist  = lambda: list(map(int, finp().split()))
slist  = lambda: list(input())
slists = lambda: input().split()
ivars  = lambda: map(int, finp().split())
ipt    = lambda: int(finp())
out    = []
#=============================================#
def sol():
    n,q = ivars()
    a = ilist()
    a.sort()
    s = set()
    for i in a:
        x = i
        while x in s:
            s.remove(x)
            x += 1
        s.add(x)
    arr = [0]* (200000 * (math.ceil(math.log2(200000)) + 10))
    for k in s:
        arr[k] = 1






#=============================================#

class SegmentTree:
    def __init__(self, length):
        self.size = 1
        self.neutral = INF
        while self.size < length: self.size *= 2
        self.arr = [self.neutral]*(self.size*2)

    def op(self, a, b):
        return min(a, b)

    def _build(self, arr, x, lx, rx):
        if rx - lx == 1:
            if lx < len(arr):
                self.arr[x] = arr[lx]
            return
        m = (rx + lx)//2
        self._build( arr, 2*x + 1, lx, m)
        self._build( arr, 2*x + 2, m, rx)
        self.arr[x] = self.op(self.arr[2*x + 1], self.arr[2*x + 2])

    def build(self, arr):
        self._build(arr, 0, 0, self.size)

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

        # going back up the tree
        self.arr[x] = self.op(self.arr[2*x + 1], self.arr[2*x + 2])

    def set(self, i, v):
        self._set(i, v, 0, 0, self.size)

    def _query(self, l, r, x, lx, rx):
        if lx >= r or l >= rx: return self.neutral # outside borders
        if lx >= l and rx <= r: return self.arr[x]
        m = (lx + rx) // 2
        a1 = self._query(l, r, 2*x + 1, lx, m)
        a2 = self._query(l, r, 2*x + 2, m, rx)
        return self.op(a1, a2) # going back up tree

    def query(self, l, r):
        # l <= i < r
        return self._query(l, r, 0, 0, self.size)

if __name__ == "__main__":
    #for _ in range(ipt()): sol()
    #sol()
    pass



