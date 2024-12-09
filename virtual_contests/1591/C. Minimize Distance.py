import sys, math
from collections import deque, defaultdict, Counter


MOD       = 10**9 + 7
INF       = float('inf')
NINF      = float('-inf')
YES, NO   = "YES", "NO"
MT        = True

#---------------------------------------------------
def sol():
    n,k = ivars()
    a = ilist()
    if n == 0:
        print(abs(a[0]))
        return
    a.sort()
    dist = 0
    start_left = 0
    for i in range(n):
        if a[i] >= 0:
            start_left = i
            break
    else:
        start_left = n
    start_right = start_left
    steps = 0

    if start_right < n - k:
        for i in range(start_right, n - k):
            if a[i] == 0: continue
            steps += 1
            if steps == k or i == n - k - 1:

                dist += a[i] * 2
                steps = 0

    steps = 0
    if start_left - 1 > k - 1:
        for i in range(start_left - 1, k - 1, -1):
            if a[i] == 0: continue
            steps += 1
            if steps == k or i == k:
                dist += a[i] * 2
                steps = 0

    max_left = 0
    max_right = max(0, a[n - 1])
    if a[0] < 0:
        max_left = abs(a[0])

    print(dist + min(max_left, max_right) * 2 + max(max_left, max_right))


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

