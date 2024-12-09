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
    if n == 0: return 0
    if n == 1: return 2
    if n == 2: return 2
    if n <= 6: return 3

    left, right = 0, 10**9 + 5
    result = -1

    while left <= right:
        mid = (left + right) // 2

        if ((pow((3 * mid) + 2, 2) - 1) // 3) * 2 < n :
            result = mid
            left = mid + 1
        else:
            right = mid - 1
    result = (3*result) + 2
    delta1 = (result//3) * 2 + 2
    r1 = (pow(result, 2)// 3)
    if (r1 + delta1)*2 >= n:
        return result + 1
    if (r1 + delta1 + delta1) * 2 >= n:
        return result + 2
    return result + 3




#---------------------------------------------------


if __name__ == "__main__":
    for _ in range(ipt()): print(sol())
    #sol()
    pass

'''
0, 2, 6, 10, 16, 24, 32, 42, 54, 66
0   2   4   4   6   8   8   10   12   12   14   16   16
  2   2   0   2   2   0   2    2    0    2    2    0

1  2  3  4   5   6   7  8   9   10
0  1  2  2   3   4   4  5   6    6
   1     2   3       4  5        6
      2          4          6
      1          2          3

 1  2  3 ->  3
 4  5  6 ->  9
 7  8  9 -> 15
10 11 12 -> 21

1 2 3  4  5  6  7  8  9 10
0 2 6 10 16 24 32 42 54 66
0 1 3  5  8 12 16 21 27 33 40 48 56

3      6       9         12
4      25      64        121

deltas:
3 ->  4 => 2 ( +1 if 1 mod 3; +2 if 2 mod 3 )
6 ->  7 => 4
9 -> 10 => 6
sum of every 3 is sum (3k + 2)**2

1 2 3 4 5 6 7 8
0 2 6

'''
