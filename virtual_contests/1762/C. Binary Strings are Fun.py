import sys, math
from collections import deque, defaultdict, Counter

MOD       = 998_244_353
INF       = float('inf')
NINF      = float('-inf')
YES, NO   = "YES", "NO"
MT        = True

#---------------------------------------------------
def sol():
    n = ipt()
    s = slist()
    res = 1
    prev = 1
    for i in range(1, n):
        if s[i] == s[i-1]:
            res += prev * 2
            prev *= 2
        else:
            res += 1
            prev = 1
        res %= MOD
        prev %= MOD
    print(res)



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
n = 3
s = 010

0 -> 1
01
0_1 -> 1
010
0_1_0 -> 1

n = 9
101101111
1 -> 1
1_0 -> 1
1_0_1 -> 1
1_0_1_1 -> 2
1_0_1_1_0 -> 1
1_0_1_1_0_1 -> 1
1_0_1_1_0_1_1 -> 2
1_0_1_1_0_1_1_1 -> 4
1_0_1_1_0_1_1_1_1 -> 8
'''
