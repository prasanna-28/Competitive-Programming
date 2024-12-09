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
    b = [a[0]]
    for i in range(1, n):
        if a[i] != b[-1]:
            b.append(a[i])

    peaks = 0
    for i in range(len(b)):
        y = True
        if i > 0:
            y &= b[i] > b[i-1]
        if i < len(b) - 1:
            y &= b[i] > b[i+1]
        peaks += y
    print(YES if peaks <= 1 else NO)

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

