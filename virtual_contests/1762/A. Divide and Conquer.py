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
    if not sum(a) & 1:
        print(0)
        return

    odd = []
    even = []
    for i in a:
        if i == 0: continue
        if i&1:
            odd.append(i)
        else:
            even.append(i)

    odd_min = INF
    even_min = INF
    for i in odd:
        k = list(reversed(bin(i)[2:].zfill(32)))
        ct = 0
        while k[ct] != '0':
            ct += 1
        odd_min = min(odd_min, ct)

    for i in even:
        k = list(reversed(bin(i)[2:].zfill(32)))
        ct = 0
        while k[ct] != '1':
            ct += 1
        even_min = min(even_min, ct)
    print(min(even_min, odd_min))


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

