import sys, math
from collections import deque, defaultdict, Counter

MOD       = 10**9 + 7
INF       = float('inf')
NINF      = float('-inf')
YES, NO   = "YES", "NO"
MT        = True

def query(a, b):
    print("?", a, b, flush = True)
    res = ipt()
    if not ~res: exit(0)
    return res

def answer(x):
    print("!", x, flush = True)

#---------------------------------------------------
def sol():
    n = ipt()
    poss = list(range(1, (pow(2, n)) + 1))
    while len(poss) > 1:
        if len(poss) == 2:
            res = query(poss[0], poss[1])
            if res == 1:
                answer(poss[0])
            else:
                answer(poss[1])
            return
        newposs = []
        for i in range(0, len(poss), 4):
            a1 = poss[i]
            a2 = poss[i+1]
            b1 = poss[i+2]
            b2 = poss[i+3]
            first = query(a1, b1)
            if first == 0: # a1 == b1
                second = query(a2, b2)
                if second == 1: # a2 > b2
                    newposs.append(a2)
                elif second == 2: # b2 > a2
                    newposs.append(b2)
            elif first == 1: # a1 > b1
                second = query(a1, b2)
                if second == 1: # a1 > b2
                    newposs.append(a1)
                elif second == 2: # b2 > a1
                    newposs.append(b2)
            else: # b1 > a1
                second = query(a2, b1)
                if second == 1: # a2 > b1
                    newposs.append(a2)
                elif second == 2: # b1 > a2
                    newposs.append(b1)
        poss = newposs
    answer(poss[0])
    return



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
2 0 1 0

query(x, y)
if 0 -> query other two
if 1 or 2 -> query the larger one with the other one
'''
