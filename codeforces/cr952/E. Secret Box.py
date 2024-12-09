import sys, math
from collections import deque, defaultdict, Counter

MOD       = 10**9 + 7
INF       = float('inf')
NINF      = float('-inf')
YES, NO   = "YES", "NO"
MT        = True

#---------------------------------------------------
def sol():
    x,y,z,k = ivars()
    ans = None
    mn = INF
    C = k ** (1/3)
    C = int(C)
    test = list(sorted([x,y,z]))
    for i in range(1, C + 3):
        for j in range(i, C + 3):
            if k % (i*j) == 0:
                curr = list(sorted([i, j, k//(i*j)]))
                if any([t > l for t,l in zip(curr, test)]):
                    continue
                if ans == None or max(i, j, k // (i*j)) - min(i, j, k // (i*j)) < mn:
                    ans = [(i, j, k//(i*j))]
                    mn = max(*(ans[0])) - min(*(ans[0]))
                elif max(i, j, k//(i*j)) - min(i, j, k//(i*j)) == mn:
                    ans.append((i, j, k//(i*j)))
    res = 1
    if ans == None:
        print(0)
        return
    for i in ans:
        curr = 1
        i = list(i)
        i.sort()
        for j in range(3):
            if test[j] >= i[j]:
                curr *= (test[j] - i[j] + 1)
            else:
                break
        else:
            res = max(res, curr)
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

