import sys
from bisect import bisect_right
from itertools import combinations
from functools import cache

MOD       = 10**9 + 7
INF       = float('inf')
NINF      = float('-inf')
YES,NO    = "YES", "NO"
DEBUG     = 0
CONTRACTS = 1
MT        = 1
OUT       = []

facts = [6]
i = 4
while facts[-1] < pow(10, 12):
    facts.append(facts[-1] * i)
    i += 1
powerful = []

for i in range(1, len(facts) + 1):
    for comb in combinations(facts, i):
        powerful.append((sum(comb), i))

powerful.sort(key = lambda x: x[0])

#---------------------------------------------------
@cache
def sol(n):
    end = bisect_right(powerful, n, key = lambda x: x[0])
    mn = oneCount(n)
    for k in range(end + 1):
        mn = min(mn, oneCount(n - powerful[k][0]) + powerful[k][1])
    return mn

def oneCount(b):
    if b < 0:
        return INF
    bitcount = 0
    while b > 0:
        bitcount += b & 1
        b >>= 1
    return bitcount

#---------------------------------------------------
def main():
    if MT:
        for _ in range(ipt()):
            print(sol(ipt()))
    else:
        sol()

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
    debug       = lambda **kwargs: (print("Dbg:"), print("\n".join([f"{key} = {value}" for key, value in kwargs.items()]))) if DEBUG else None

    main()

