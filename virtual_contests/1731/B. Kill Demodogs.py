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
    n_1 = n + 1
    tn_1 = 2*n + 1
    res = 2 * (n * n_1 * tn_1)//6 - (n*(n_1))//2
    print((res * 2022) % MOD)


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
1*1 + 2*3 + 3*5 + 4*7 + ... + n * (2n - 1)
sum of all 2n^2 - n
2 * (sum[n^2]) - (n*(n+1))//2
2 * (n)(n+1)(2n+1)/6 - (n)(n+1)/2
'''
