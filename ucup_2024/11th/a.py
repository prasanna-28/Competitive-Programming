import sys

MOD = 998244353

def main():

    def read():
        return sys.stdin.read()

    dta = list(map(int, read().split()))
    T = dta[0]
    qry = dta[1:T+1]

    tgtA = 'NPCAPC'
    tgtB = 'npcapc'
    lenA = len(tgtA)
    lenB = len(tgtB)

    slst = [(i, j) for i in range(lenA +1) for j in range(lenB +1)]
    smap = { (i,j): idx for idx, (i,j) in enumerate(slst) }
    tsts = len(slst)

    trans = [[0] * tsts for _ in range(tsts)]

    for i, j in slst:
        cidx = smap[(i, j)]

        if i < lenA:
            ni = i + 1
            nj = j
            nidx = smap[(ni, nj)]
            trans[nidx][cidx] += 1

        if j < lenB:
            ni = i
            nj = j + 1
            nidx = smap[(ni, nj)]
            trans[nidx][cidx] += 1

        nmtch = 52
        if i < lenA:
            nmtch -= 1
        if j < lenB:
            nmtch -= 1
        trans[cidx][cidx] += nmtch % MOD

    def mmul(a, b):
        res = [[0]*len(b[0]) for _ in range(len(a))]
        for x in range(len(a)):
            for y in range(len(b)):
                if a[x][y]:
                    for z in range(len(b[0])):
                        res[x][z] = (res[x][z] + a[x][y] * b[y][z]) % MOD
        return res


    precp = []
    cpow = [row[:] for row in trans]
    precp.append(cpow)
    for _ in range(1, 32):
        cpow = mmul(cpow, cpow)
        precp.append(cpow)

    for N in qry:
        dp = [0] * tsts
        dp[smap[(0, 0)]] = 1

        pwr = 0
        while N > 0:
            if N & 1:
                ndp = [0] * tsts
                mat = precp[pwr]
                for x in range(tsts):
                    if dp[x]:
                        for y in range(tsts):
                            ndp[y] = (ndp[y] + mat[y][x] * dp[x]) % MOD
                dp = ndp
            N >>= 1
            pwr += 1

        ans = dp[smap[(lenA, lenB)]]
        print(ans)

if __name__ == "__main__":
    main()

