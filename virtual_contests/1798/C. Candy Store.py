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
    a = []
    b = []
    for _ in range(n):
        ai,bi = ivars()
        a.append(ai)
        b.append(bi)

    streaks = 0
    curr_gcd = a[0] * b[0]
    curr_lcm = b[0]

    for i in range(1, n):
        if (u:=math.gcd(curr_gcd, a[i] * b[i])) % (v:=math.lcm(curr_lcm, b[i])) == 0:
            streaks += 1

            curr_gcd = u
            curr_lcm = v
        else:
            curr_gcd = a[i] * b[i]
            curr_lcm = b[i]
    print(n - streaks)




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

