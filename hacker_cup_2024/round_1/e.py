INPUT_FILE = ""
OUTPUT_FILE = ""

import sys
from collections import deque

def solve(t):
    n = int(input())
    trie = [{}]
    for _ in range(n):
        idx = 0
        s = input()
        for i in s:
            if i == '?':
                if '?' not in trie[idx]:
                    sizes[idx] = 26 - len(trie[idx].keys())
                    trie[idx]['?'] = len(trie)
                    idx = trie[idx]['?']
                else:
                    idx = trie[idx]['?']
            else:
                if '?' in trie[idx]:
                    idx = trie[idx]['?']
                elif i in trie[idx]:
                    idx = trie[idx][i]
                else:
                    trie[idx][i] = len(trie)
                    trie.append({})
                    idx = trie[idx][i]
    total = 1

    q = deque([0])
    while q:
        idx = q.popleft()


with open(INPUT_FILE, 'r') as f:
    sys.stdin = f
    for i in range(int(input())):
        solve(i)
