import sys
import math
import operator
from collections import deque, defaultdict, Counter, OrderedDict
from functools import cache, partial, reduce
from itertools import *
from bisect import bisect_left, bisect_right

MOD       = 10**9 + 7
INF       = float('inf')
NINF      = float('-inf')
YES,NO    = "YES", "NO"
DEBUG     = 0
CONTRACTS = 1
MT        = 1
OUT       = []

#---------------------------------------------------


def sol():
    n,c = ivars()
    a = ilist()
    a.sort()
    check = set(map(str, a))
    if '1' not in check:
        OUT.append(NO)
        return
    for i,v in enumerate(reversed(a)):
        j = 0
        i = n - i - 1
        while j < i and j != -1:
            if str(v//a[j]) not in check:
                OUT.append(NO)
                return
            # new j is smallest idx such that v//a[idx] < v//a[j]
            j = fsi(a, j , i+1, v, v//a[j])
    OUT.append(YES)

def fsi(a, left, right, CONSTANT, target):
    left, right = 0, len(a) - 1
    result = -1

    while left <= right:
        mid = (left + right) // 2
        if CONSTANT // a[mid] < target:
            result = mid
            right = mid - 1
        else:
            left = mid + 1

    return result
#---------------------------------------------------
def main():
    if MT:
        for _ in range(ipt()):
            sol()
        print(njoin(OUT))
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
'''
assume x//y in a
x//(x//y) must be in a
y//(x//y) must be in a
1 must be in array (need stopping point for x//y...)

let a//b be in array and b//c be in array
a//c must also be in the array

is there a necessary and sufficient condition?

'''

