import sys, math
from collections import deque, defaultdict, Counter
from bisect import bisect_left

MOD       = 10**9 + 7
INF       = float('inf')
NINF      = float('-inf')
YES, NO   = "YES", "NO"
MT        = True
MAX_N     = pow(10, 5)

squares = []
for i in range(math.isqrt(MAX_N) * 4):
    squares.append(i**2)

#---------------------------------------------------
def sol():
    n = ipt()
    res = [0] * n
    i = n - 1
    while i >= 0:
        curr = i
        l = bisect_left(squares, curr)
        for _ in range(curr, squares[l] - curr - 1, -1):
            res[i] = squares[l] - i
            i -= 1
    print(ljoin(res))


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

'''
18 17 16 15 14 13 12 11 10  9  8  7  6  5  4  3  2  1  0
 7  8  9 10 11 12 13 14 15 16 17 18  3  4  5  6  2  0  1
'''
