import sys, math
from collections import deque, defaultdict, Counter

MOD       = 10**9 + 7
INF       = float('inf')
NINF      = float('-inf')
YES, NO   = "YES", "NO"
MT        = True
out = []
k = 0
#---------------------------------------------------
def sol():
    n = ipt()
    a = ilist()
    # curr_size, max_so_far, start_index, max_from_start
    track = [INF] * (n+1)
    track[n] = 0
    max_so_far = [0] * (n + 1)
    mx = 0

    for i in range(n-1, -1, -1):
        max_so_far[i] = mx
        if i + a[i] + 1 > n: continue
        track[i] = track[a[i] + 1 + i] + 1
        max_so_far[i] = mx
        max_so_far[i] = max(max_so_far[i], max_so_far[i + a[i] + 1] + 1)
        if track[i] != INF:
            mx = max(mx, track[i])

    res = [2] * (n-1)
    for i in range(n-2, -1, -1):
        if track[i+1] == a[i]:
            res[i] = 0
            continue
        if track[i+1] != INF:
            res[i] = 1
            continue
        if max_so_far[i+1] >= a[i] - 1:
            res[i] = 1
            continue

    print(ljoin(res))


def sol2():
    n = ipt()
    a = ilist()
    # (is_test, test_length, max_so_far, path)
    # (is_test = i + a[i] == n OR a[i + a[i]] is_test, cond1 -> length is 1 ; cond2 -> length is prev test + 1)
    # track[n-1] = [0, 0] if a[n-1] != 0 else [1, 1]
    # track[n-2] =
    #
    global k
    max_so_far = 0
    track = [[0,0,0,None, 0] for _ in range(n)]

    for i in range(n-1, -1, -1):

        cond1 = i + a[i] + 1 == n
        cond2 = 0
        val = 0
        change = None
        dist = 0
        if i + a[i] + 1 < n:
            cond2 = track[i+a[i] + 1][0]
            val = track[i+a[i] + 1][1]
            change = i + a[i] + 1
            dist = track[i+a[i] + 1][4] + 1
        if cond1:
            track[i] = [1,1,max_so_far, i, dist]
            max_so_far = max(max_so_far, 1)
        elif cond2:
            track[i] = [1, val + 1, max_so_far, change, dist]
            max_so_far = max(max_so_far, val+1)
        else:
            track[i] = [0,0,max_so_far, change, dist]

    print(track)

    res = [0] * (n-1)
    for i in range(n-1):
        if a[i] == track[i+1][1]:
            res[i] = 0
            continue
        if track[i+1][1] != 0:
            res[i] = 1
            continue
        if track[i+1][2] >= a[i] - 1:
            res[i] = 1
            continue
        if track[i+1][3] != None:
            if a[i] - track[i+1][4] - 1 <= track[track[i+1][3]][2]:
                res[i] = 1
                continue
        res[i] = 2
    k += len(res)
    if k >= 129967:
        print(ljoin(a))
    out.append(ljoin(res))





#---------------------------------------------------
def main():
    for _ in range(ipt() if MT else 1): sol()
    # print(ljoin(out))

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


