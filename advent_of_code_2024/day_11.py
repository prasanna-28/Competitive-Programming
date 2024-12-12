d = map(int, input().split())
k = int(input())
res = 0

from functools import cache

@cache
def dp(num, k):
    if k == 0:
        return 1
    if num == 0:
        return dp(1, k -1)
    if len(str(num)) % 2 == 0:
        return dp(int(str(num)[:len(str(num))//2]), k - 1) + dp(int(str(num)[len(str(num))//2:]), k - 1)
    return dp(num * 2024, k - 1)

for i in d:
    res += dp(i, k)
print(res)
