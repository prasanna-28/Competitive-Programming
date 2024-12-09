import sys, math
from collections import deque, defaultdict, Counter

MOD       = 10**9 + 7
INF       = float('inf')
NINF      = float('-inf')
YES, NO   = "YES", "NO"
MT        = True

#---------------------------------------------------
def sol():
    n, c = ivars()
    a = ilist()
    res = [0] * n
    pref = [0]
    mx_f = [0]
    mx_b = [0]
    for i in a:
        mx_f.append(max(mx_f[-1], i))
        pref.append(pref[-1] + i)
    for i in reversed(a):
        mx_b.append(max(mx_b[-1], i))
    mx_b.reverse()
    if a[0] + c < mx_b[0] and a[0] != mx_b[0]:
        res[0] = 1
    for i in range(1, n):
        mx_after = mx_b[i]
        mx_before = mx_f[i]
        if a[i] == mx_after and a[i] > mx_before and a[0] + c < a[i]:
            continue
        else:
            res[i] += i
            if pref[i + 1] + c < mx_after:
                res[i] += 1
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

