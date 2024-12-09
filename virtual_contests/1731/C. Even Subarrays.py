import sys, math
from collections import deque, defaultdict, Counter
from bisect import bisect_left

MOD       = 10**9 + 7
INF       = float('inf')
NINF      = float('-inf')
YES, NO   = "YES", "NO"
MT        = True

max_N = 2 ** (len(bin(200000)) - 2)
squares = []
for i in range(math.isqrt(max_N) + 2):
    squares.append(i**2)
#---------------------------------------------------
def sol():
    n = ipt()
    a = ilist()
    total_subarrays = (n * (n+1))//2
    mx = max(a)
    max_square = 2**(len(bin(mx)) - 2)
    end = bisect_left(squares, max_square) + 1
    pref = [0]
    for i in a:
        pref.append(pref[-1] ^ i)
    s = set(pref)
    c = Counter(pref)
    result = 0
    for x in s:
        result += (c[x] * (c[x] - 1))
    for i in range(1, min(end + 1, len(squares))):
        for x in s:
            result += c[x^squares[i]] * c[x]
    print(total_subarrays - (result // 2))

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

