import   sys, math
MOD    = 10**9 + 7
INF    = float('inf')
NINF   = float('-inf')
YES,NO = "YES", "NO"
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
    n,x = ivars()
    a = ilist()
    if x <= n//2:
        print(YES)
        return
    res = []
    for i in range(n-x):
        res.append(a.pop())
    a.reverse()
    for i in range(n-x):
        res.append(a.pop())
    if len(res) != 0:
        res.sort()
        small = res[(len(res) - 1) // 2]
        big   = res[(len(res) + 1) // 2]
        for i in a:
            if i < small or i > big:
                print(NO)
                return
    a.reverse()
    print(YES if list(sorted(a)) == a else NO)



#-----------------------------------------------
if __name__ == "__main__":
    for _ in range(ipt()): sol()
    #sol()
    pass






