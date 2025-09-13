def binary_search(lo, hi, cond):
    while lo < hi:
        mid = (lo + hi) // 2
        res = cond(mid)
        if res == 0:
            return mid
        elif res < 0:
            hi = mid
        else:
            lo = mid + 1
    return -1

