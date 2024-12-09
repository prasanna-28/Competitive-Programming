import   sys, math
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

#-----------------------------------------------
def sol():
    n, H = ivars()
    a = ilist()
    a.sort(reverse = True)
    m1 = a[0]
    m2 = a[1]
    tot = m1 + m2
    steps = H // tot
    steps *= 2
    H = H % tot
    start = 0
    while H > 0:
        if start:
            H -= m2
        else:
            H -= m1
        start = not start
        steps += 1
    print(steps)

#-----------------------------------------------
if __name__ == "__main__":
    for _ in range(ipt()): sol()
    #sol()
    pass



