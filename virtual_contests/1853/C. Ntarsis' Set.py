
import   sys, math
finp   = sys.stdin.readline
MOD    = 10**9 + 7
njoin  = lambda x: '\n'.join(map(str, x))
ljoin  = lambda x: ' '.join(map(str, x))
sjoin  = lambda x: '\n'.join(x)
initl  = lambda x,y: [y]*x
INF    = float('inf')
NINF   = float('-inf')
ilist  = lambda: list(map(int, finp().split()))
slist  = lambda: list(input())
slists = lambda: input().split()
ivars  = lambda: map(int, finp().split())
ipt    = lambda: int(finp())
out    = []
#=============================================#
def sol():
    n,k = ivars()
    a = ilist()
    i = 0
    start = 1
    for _ in range(k):
        while i < n and start + i>= a[i]:
            i += 1
        start += i

    print(start)



#=============================================#

if __name__ == "__main__":
    for _ in range(ipt()): sol()
    #sol()
    pass

'''
1  -  1  2  6
3  -  3  7 12
4  -  4  8 13
5  -  5  9 14
10 - 10 15 20

6 11 12 13 14 16 17 18 19 20 21 22 23 24

after some number of iterations, the difference normalizes

lets check the last case

 1  3  4  5  10  11  12  13  14  15 k = 1
 2  7  8  9  20  21  22  23  24  25 k = 2
 6 17 18 19  30  31  32  33  34  35 k = 3
16 27 28 29  40  41  42  43  44  45 k = 4

149998*10 + 6

10x + 9y + 8z + ... k = n

16 20 27 28 29 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50


  1  7 10
  1  7 10
  2  9 13
  3 12 16
  4 15 19
  5 18 22
  6 21 25
  8 24 28
 11 27 31
 14

5 6 8 11 14 17 18 20 21 22 23 24 25 26

1 4 7 9 12 17 18 20


last one skips by n, second to last n-1, third to last n-2, and so on (unless chain)

the maximum difference between two consecutive numbers is the maximum number of days it takes for the skips to consolidate (consecutive is 0)

1 3 6

first skip by 1
then skip by 3
lastly skip by 6



'''


