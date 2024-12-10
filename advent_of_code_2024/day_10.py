from collections import deque
res = 0
n = m = 45
grid = []
for i in range(n):
    grid.append(list(map(int, list(input()))))
for i in range(n):
    for j in range(m):
        if grid[i][j] != 0: continue
        q = deque([(i, j)])
        while q:
            x, y = q.popleft()
            if grid[x][y] == 9:
                res += 1
                # for part 1, remove res += 1 and add (x, y) to a set defined after the queue
                # outside of the while loop, add the length of the set to res
            else:
                dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for dx, dy in dirs:
                    if 0 <= x + dx < n and 0 <= y + dy < m:
                        nextx, nexty = x + dx, y + dy
                        if grid[nextx][nexty] == grid[x][y] + 1:
                            q.append((nextx, nexty))
print(res)
