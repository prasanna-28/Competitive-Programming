
import sys, math
from collections import deque, defaultdict, Counter
FILE = "a_tests/subsonic_subway_input.txt"

MOD       = 10**9 + 7
FASTIO    = False
DEBUG     = False
INF       = float('inf')
NINF      = float('-inf')
YES, NO   = "YES", "NO"
MT        = True

#====================Solution====================
def sol(t):
    n = int(input())
    a = []
    b = []
    for _ in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    min = NINF
    for i, bi in enumerate(b):
        if (i + 1)/bi >= min:
            min = (i + 1)/bi

    for i in range(n):
        ai, bi = a[i], b[i]
        if not (ai <= (i + 1) / min <= bi):
            min = -1
            break
    with open("output.txt", 'a') as fi:
        fi.write(f"Case #{t + 1}: {min}\n")
#================================================

def main():
    with open(FILE, 'r') as f:
        sys.stdin = f
        for i in range(int(input()) if MT else 1):
            sol(i)


def debug(*args):
    if DEBUG:
        for arg in args:
            print(arg)

def ASSERT(cond):
    if DEBUG:
        assert(cond)


if FASTIO:
    pass

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

