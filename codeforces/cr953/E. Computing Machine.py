import sys, math
from collections import deque, defaultdict, Counter
from bisect import bisect_left

MOD       = 10**9 + 7
INF       = float('inf')
NINF      = float('-inf')
YES, NO   = "YES", "NO"
MT        = True

#---------------------------------------------------
def sol():
    n = ipt()
    s = list(map(int, input()))
    t = list(map(int, input()))
    q = ipt()
    track = []
    check = []

    for i in range(1, len(s) - 1):
        if not s[i]:
            if t[i - 1]:
                needleft = i - 1
            elif 1 < i and not s[i - 2]:
                needleft = i - 2
            else:
                continue
            if t[i + 1]:
                needright = i + 1
            elif i < len(s) - 2 and not s[i + 2]:
                needright = i + 2
            else:
                continue
            check.append(i)
            track.append((i, needleft, needright))
    for i in range(n):
        if s[i]:
            track.append((i, i, i))
            check.append(i)
    track.sort()
    check.sort()
    # print(track)
    # print(check)
    for _ in range(q):
        l,r = ivars()
        left = l - 1 # include
        right = r    # exclude
        il = bisect_left(check, left)
        ir = bisect_left(check, right)
        #        print(left, right, il, ir)
        res = ir - il
        #print('len', res)
        if res < 5:
            for idx in range(il, ir):
                i, nl, nr = track[idx]
                if nl < left or nr >= right:
                    res -= 1
        else:
            l1 = il
            l2 = il + 1
            r2 = ir - 2
            r1 = ir - 1
            checks = [l1, l2, r2, r1]
            for idx in checks:
                i, nl, nr = track[idx]
                if nl < left or nr >= right:
                    res -= 1
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
0101010
0001010
'''
