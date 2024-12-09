import sys, math
from collections import deque, defaultdict, Counter

MOD       = 10**9 + 7
INF       = float('inf')
NINF      = float('-inf')
YES, NO   = "YES", "NO"
MT        = True

#---------------------------------------------------
def sol():
    N,M = ivars()
    matrix = []
    for _ in range(N):
        matrix.append(ilist())
    table = [[[[0 for l in range(int(math.log2(M)) + 1)] for k in range(
    int(math.log2(N)) + 1)] for j in range(M)] for i in range(N)]

    def build_sparse(n, m):
        for i in range(n):
            for j in range(m):
                table[i][j][0][0] = matrix[i][j]

        for k in range(1, int(math.log2(n)) + 1):
            for i in range(n - (1 << k) + 1):
                for j in range(m - (1 << k) + 1):
                    table[i][j][k][0] = min(
                        table[i][j][k-1][0], table[i+(1 << (k-1))][j][k-1][0])

        for k in range(1, int(math.log2(m)) + 1):
            for i in range(n):
                for j in range(m - (1 << k) + 1):
                    table[i][j][0][k] = min(
                        table[i][j][0][k-1], table[i][j+(1 << (k-1))][0][k-1])

        for k in range(1, int(math.log2(n)) + 1):
            for l in range(1, int(math.log2(m)) + 1):
                for i in range(n - (1 << k) + 1):
                    for j in range(m - (1 << l) + 1):
                        table[i][j][k][l] = min(
                            table[i][j][k-1][l-1],
                            table[i+(1 << (k-1))][j][k-1][l-1],
                            table[i][j+(1 << (l-1))][k-1][l-1],
                            table[i+(1 << (k-1))][j+(1 << (l-1))][k-1][l-1]
                        )
    def rmq(x1, y1, x2, y2):

        k = int(math.log2(x2-x1+1))
        l = int(math.log2(y2-y1+1))

        return min(
            table[x1][y1][k][l],
            table[x2-(1 << k)+1][y1][k][l],
            table[x1][y2-(1 << l)+1][k][l],
            table[x2-(1 << k)+1][y2-(1 << l)+1][k][l]
        )

    build_sparse(N,M)

    def works(l):
        for i in range(N - l + 1):
            for j in range(M - l + 1):
                #print(i, j, i + l - 1, j + l - 1)
                if (rmq(i , j, i + l - 1, j + l - 1)) >= l:
                #    print(u)
                    res = l
                    return True
                #print(u)
            else:
                continue
            break
        return False
    left = 1
    right = min(N,M) + 1
    while left < right:
        mid = left + (right - left) // 2
        if works(mid):
            left = mid + 1
        else:
            right = mid
    print(left - 1)


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

