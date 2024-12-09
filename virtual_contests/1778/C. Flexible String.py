import sys, math
from collections import deque, defaultdict, Counter
from itertools import combinations

MOD       = 10**9 + 7
INF       = float('inf')
NINF      = float('-inf')
YES, NO   = "YES", "NO"
MT        = True
MAX_N     = 100001

lens = [0] * MAX_N
for i in range(MAX_N):
    lens[i] = (i * (i+1))//2

#---------------------------------------------------
def sol():
    n, k = ivars()
    a = input()
    b = input()
    check = set(a)
    k = min(k, len(check))
    res = 0
    for letters in combinations(check, k):
        seen = set(letters)
        ct = 0
        currln = 0
        i = 0
        while i < n:
            if a[i] in seen or a[i] == b[i] :
                currln += 1
            else:
                ct += lens[currln]
                currln = 0
            i += 1
        ct += lens[currln]
        res = max(res, ct)
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

