import   sys, math
from collections import Counter
MOD    = 10**9 + 7
INF    = float('inf')
NINF   = float('-inf')
YES,NO = "Yes", "No"
DEBUG  = 0
finp   = sys.stdin.readline
njoin  = lambda x: '\n'.join(map(str, x))
ljoin  = lambda x: ' '.join(map(str, x))
sjoin  = lambda x: '\n'.join(x)
ilist  = lambda: list(map(int, finp().split()))
slist  = lambda: list(input())
slists = lambda: input().split()
ivars  = lambda: map(int, finp().split())
ipt    = lambda: int(finp())
debug  = lambda **kwargs: (print("Dbg:"), print("\n".join([f"{key} = {value}" for key, value in kwargs.items()]))) if DEBUG else None

#---------------------------------------------------
def sol():
    n = ipt()
    a = ilist()
    steps = [a]
    while True:
        curr = steps[-1][:]
        counts = Counter(curr)
        for i in range(len(curr)):
            curr[i] = counts[curr[i]]
        if curr != steps[-1]:
            steps.append(curr)
        else:
            break
    for _ in range(ipt()):
        x,k = ivars()
        if k >= len(steps): k = len(steps) - 1
        print(steps[k][x-1])



#---------------------------------------------------
if __name__ == "__main__":
    for _ in range(ipt()): sol()
    #sol()
    pass
