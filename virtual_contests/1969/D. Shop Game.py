import   sys, math
import heapq
hpop = heapq.heappop
hpush = heapq.heappush
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
    n,k = ivars()
    a,b = ilist(), ilist()
    c = list(enumerate(b)).sort(key = lambda x: x[1], reverse = True)
    tot = 0
    take = []
    for i in c:
        if i[1] - a[i[0]] > 0:
            take.append(i[0])
            tot += i[1] - a[i[0]]

    if len(take) <= k:
        print(0)
        return
    if k == 0:
        print(tot)
        return
    h = []
    heapq.heapify(h)
    for i in range(k):
        hpush(h, (-a[take[i]], -(b[take[i]] - a[take[i]])))
        tot -= b[take[i]] - a[take[i]]
        tot -= a[take[i]]
    for i in range(k, len(take)):
        i = take[i]
        curr_a = a[i]
        curr_profit = b[i] - a[i]
        curr_max_a = -hpop(h)
        if curr_a < curr_max_a
#---------------------------------------------------
if __name__ == "__main__":
    for _ in range(ipt()): sol()
    #sol()
    pass


'''
assume alice buys everything where a[i] < b[i]
profit is sum(a[i] - b[i])
alice does not want to take large values of a[i]
if bob takes for free, alice loses a[i], and the potential profit of b[i] - a[i] -> alice loses b[i]
if bob buys, alice gains nothing (potential profit is already calculated)

what does alice want to take/not take?
alice wants to maximize b[i] - a[i]
alice wants to minimize a[i]

if b[j] - a[j] > a[i], bob will take b[j] - a[j]
if a[i] > b[j] - a[j], bob will take a[i]
if they are equal, it doesn't matter which one bob takes

if sum of highest k a[i] > sum of the rest b[j] - a[j], alice will not take the highest a[i]
maximum of all of these values is the result
sum of highest k (a[i] or b[j] - a[j]) - rest is result
slowly pop highest each time to get the maximum possible result
'''
