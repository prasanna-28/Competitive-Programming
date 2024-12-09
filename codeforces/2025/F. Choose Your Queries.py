n, q = map(int, input().split())
qry = []
fcnt = [0] * (n + 1)

occ = [[] for _ in range(n + 1)]

for i in range(q):
    x, y = map(int, input().split())
    qry.append((x, y))
    occ[x].append(i)
    occ[y].append(i)

fcnt_qry = []
cur_fcnt = [0] * (n + 1)

for i in range(1, n + 1):
    cur_fcnt[i] = len(occ[i])

for i in range(q):
    x, y = qry[i]
    fcnt_qry.append((cur_fcnt[x], cur_fcnt[y]))
    cur_fcnt[x] -= 1
    cur_fcnt[y] -= 1

cnt = [0] * (n + 1)
res = []

for i in range(q):
    x, y = qry[i]
    x_fut, y_fut = fcnt_qry[i]

    if cnt[x] > 0 and cnt[y] > 0:
        if x_fut <= y_fut:
            cnt[x] -= 1
            res.append('x-')
        else:
            cnt[y] -= 1
            res.append('y-')
    elif cnt[x] > 0:
        cnt[x] -= 1
        res.append('x-')
    elif cnt[y] > 0:
        cnt[y] -= 1
        res.append('y-')
    else:
        if x_fut >= y_fut:
            cnt[x] += 1
            res.append('x+')
        else:
            cnt[y] += 1
            res.append('y+')

for r in res:
    print(r)

