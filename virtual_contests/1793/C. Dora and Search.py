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
    mx_tree = SparseTable(a, max, NINF)
    mn_tree = SparseTable(a, min, INF)

    l = 0
    r = n - 1

    while l < r:
        left = a[l]
        right = a[r]
        mx = mx_tree.query(l, r)
        mn = mn_tree.query(l, r)
        if left == mx or left == mn:
            l += 1
            continue
        if right == mx or right == mn:
            r -= 1
            continue
        print(l + 1, r + 1)
        return
    print(-1)
    return



#---------------------------------------------------

class SparseTable:
    def __init__(self, arr, func, neutral):
        self.n = len(arr)
        self.log = [0] * (self.n + 1)
        self.table = [[0] * (self.n + 1) for _ in range(math.ceil(math.log2(self.n)) + 1)]
        self.func = func
        self.neutral = neutral

        for i in range(self.n):
            self.log[i] = int(math.log2(i)) if i > 0 else 0

        for i in range(self.n):
            self.table[0][i] = arr[i]

        for j in range(1, math.ceil(math.log2(self.n)) + 1):
            for i in range(self.n - (1 << j) + 1):
                self.table[j][i] = self.func(self.table[j - 1][i],
                                       self.table[j - 1][i + (1 << (j - 1))])

    def query(self, left, right):
        if left > right or left < 0 or right >= self.n:
            return self.neutral

        j = self.log[right - left]
        return self.func(self.table[j][left], self.table[j][right - (1 << j) + 1])

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

