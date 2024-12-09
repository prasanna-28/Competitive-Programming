from collections import defaultdict
import sys

def main(test_case):
    line = ''
    while line.strip() == '':
        line = sys.stdin.readline()
    R, C, K = map(int, line.strip().split())
    B = []
    owner_cells = defaultdict(list)
    for i in range(1, R +1):
        while True:
            row = sys.stdin.readline()
            if row.strip() != '':
                break
        row_bunnies = list(map(int, row.strip().split()))
        for j in range(1, C +1):
            owner = row_bunnies[j -1]
            owner_cells[owner].append( (i, j) )
    owners_multi = []
    for owner, cells in owner_cells.items():
        if len(cells) >=2:
            sorted_cells = sorted(cells)
            owners_multi.append(sorted_cells)
    def sum_range(n, d):
        if d >=n:
            return n *n
        else:
            return (2*n*d + n) - d*(d +1)
    def compute_count(d):
        sum_i = sum_range(R, d)
        sum_j = sum_range(C, d)
        total_pairs = sum_i * sum_j - R * C
        same_owner_pairs =0
        for cells in owners_multi:
            s = len(cells)
            for idx in range(s):
                i1, j1 = cells[idx]
                left = idx +1
                right = s
                while left < right:
                    mid = (left + right) //2
                    if cells[mid][0] > i1 +d:
                        right = mid
                    else:
                        left = mid +1
                for jdx in range(idx +1, left):
                    i2, j2 = cells[jdx]
                    if abs(j2 - j1) <=d:
                        same_owner_pairs +=2
        return total_pairs - same_owner_pairs
    low =0
    high = max(R, C)
    answer = high
    while low <= high:
        mid = (low + high) //2
        cnt = compute_count(mid)
        if cnt >= K:
            answer = mid
            high = mid -1
        else:
            low = mid +1
    with open("output.txt", 'a') as w:
        w.write(f"Case #{test_case + 1}: {answer}\n")

FILE = 'bunny_hopscotch_input.txt'
with open(FILE, 'r') as f:
    sys.stdin = f
    for t in range(int(input())):
        print(f"test case {t}")
        main(t)
