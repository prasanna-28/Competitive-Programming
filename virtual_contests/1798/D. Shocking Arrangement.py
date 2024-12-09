import sys, math
from collections import deque, defaultdict, Counter

MOD       = 10**9 + 7
INF       = float('inf')
NINF      = float('-inf')
YES, NO   = "Yes", "No"
MT        = True

#---------------------------------------------------
def sol():
    n = ipt()
    a = ilist()
    a.sort()
    if all([i == 0 for i in a]):
        print(NO)
        return
    a = deque(a)
    res = []
    s = 0
    while len(a) > 0:
        if s < 0:
            res.append(a.pop())
            s += res[-1]
        elif s > 0:
            res.append(a.popleft())
            s += res[-1]
        else:
            res.append(a.pop())
            s += res[-1]
    print(YES)
    print(ljoin(res))



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

