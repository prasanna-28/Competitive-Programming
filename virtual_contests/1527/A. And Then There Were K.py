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

#---------------------------------------------------
def sol():
    n = ipt()
    b = bin(n)[2:]
    print(2**(len(b)-1)-1)


#---------------------------------------------------
if __name__ == "__main__":
    for _ in range(ipt()): sol()
    #sol()
    pass
