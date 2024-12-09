import sys, math
from collections import deque, defaultdict, Counter
gcd = math.gcd
MOD       = 10**9 + 7
INF       = float('inf')
NINF      = float('-inf')
YES, NO   = "YES", "NO"
MT        = True

#---------------------------------------------------
def sol():
    n = ipt()
    a = ilist()
    b = []
    b.append(a[0])
    for i in range(1, n):
        b.append(math.lcm(a[i], a[i-1]))
    b.append(a[-1])
    for i in range(n):
        if a[i] != gcd(b[i], b[i+1]):
            print(NO)
            return
    print(YES)


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

a1 a2 a3
b1 b2 b3 b4

a1 divides b1 and b2
a2 divides b2 and b3
a3 divides b3 and b4

b3 is divisible by a2 and a3
b2 is divisibe by a2 and a1

b1 = a1
b2 = lcm(a2, a1)
b3 = lcm(a2, a3)
b4 = a3

1 2 6 4 3
1 2 6 12 12

8 4 2
8 8 4 2

4 4 2 4

10 9 8 7 6 5 4 3 2 1

a1 a2 a3 a4 a5

a1 = gcd(b1, b2)
a2 = gcd(b2, b3)
a3 = gcd(b3, b4)
a4 = gcd(b4, b5)
a5 = gcd(b5, b6)
''''''
1 2


a1 a2 a3 a4 a5

a1 = gcd(b1, b2)
a2 = gcd(b2, b3)
a3 = gcd(b3, b4)
a4 = gcd(b4, b5)
a5 = gcd(b5, b6)

gcd(a1, a2) = gcd(b1, b2, b3)
gcd(a1, a2, a3) = gcd(b1, b2, b3, b4)
gcd(a1, a2, a3, a4) = gcd(b1, b2, b3, b4, b5)
'''
