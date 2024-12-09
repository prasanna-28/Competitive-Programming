import   sys, math
MOD    = 998_244_353
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
    m,n = ivars()
    a = ilist()



#---------------------------------------------------
if __name__ == "__main__":
    #for _ in range(ipt()): sol()
    sol()
    pass

'''
3 4
2 1 2
1 3 2 3
3 1 2 3
3 2 1 3
'''
