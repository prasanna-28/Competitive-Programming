import sys, math
from collections import deque, defaultdict, Counter

MOD       = 10**9 + 7
INF       = float('inf')
NINF      = float('-inf')
YES, NO   = "YES", "NO"
MT        = False



#---------------------------------------------------
def sol():
    p = ipt()
    if p == 0:
        print(0,0)
        return
    combinations = [1]
    i = 2
    while combinations[-1] < max(p, 100):
        curr = i * ( i + 1 )
        combinations.append(curr//2)
        i += 1
    dp = [INF for _ in range(p+1)]
    dp[0] = 0
    for i in range(p + 1):
        for idx, j in enumerate(combinations):
            if j <= i:
                dp[i] = min(dp[i], dp[i-j] + idx + 2)
            else:
                break
    x = dp[p]

    print(x, (x * (x-1))//2 - p)

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

