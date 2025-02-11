a = input()
n = m = len(a)
grid = [a] + [input() for _ in range(n - 1)]

seen = set()
res = 0
dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

from collections import deque

for i in range(n):
    for j in range(m):
        if (i, j) not in seen:
            seen.add((i, j))
            area = 0
            p = 0
            q = deque([(i, j)])
            while q:
                ci, cj = q.popleft()
                area += 1
                nx = set()
                ny = set()
                for dx, dy in dirs:
                    x = ci + dx
                    y = cj + dy
                    if 0 <= x < n and 0 <= y < m and grid[x][y] == grid[ci][cj]:
                        if (x, y) not in seen:
                            seen.add((x, y))
                            q.append((x, y))
                    else:
                        nx.add(dx)
                        ny.add(dy)
                if 0 in nx: nx.remove(0)
                if 0 in ny: ny.remove(0)
                p += len(nx) * len(ny)
                changes = []
                if 1 not in nx:
                    if 1 not in ny:
                        changes.append((1, 1))
                    if -1 not in ny:
                        changes.append((1, -1))
                if -1 not in nx:
                    if 1 not in ny:
                        changes.append((-1, 1))
                    if -1 not in ny:
                        changes.append((-1, -1))
                for dx, dy in changes:
                    if 0 <= ci + dx <= n and 0 <= cj + dy <= m and grid[ci + dx][cj + dy] != grid[ci][cj]:
                        p += 1
            res += area * p

print(res)

