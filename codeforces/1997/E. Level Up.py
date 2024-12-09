import sys

def binary_search(prefix_sum, i, k, a):
    left, right = 0, i
    while left < right:
        mid = (left + right) // 2
        fights = prefix_sum[i] - prefix_sum[mid]
        level_ups = fights // k

        if 1 + level_ups >= a[i]:
            right = mid
        else:
            left = mid + 1
    return left

def solve(n, q, a, queries):
    fight_counts = [1] * n
    prefix_sum = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix_sum[i] = prefix_sum[i-1] + fight_counts[i-1]

    results = []
    for i, x in queries:
        i -= 1
        fights_before = binary_search(prefix_sum, i, x, a)
        total_fights = prefix_sum[i] - prefix_sum[fights_before]
        level = 1 + total_fights // x
        results.append("YES" if level <= a[i] else "NO")
    return results

def main():
    input = sys.stdin.readline
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    queries = [tuple(map(int, input().split())) for _ in range(q)]
    results = solve(n, q, a, queries)
    print('\n'.join(results))

if __name__ == "__main__":
    main()
