INPUT_FILE = "substantial_losses_input.txt"
OUTPUT_FILE = "output.txt"

import sys

MOD = 998_244_353

def solve(t):
    w, g, l = map(int, input().split())
    l = 2 * l + 1
    w = (w * l) % MOD
    g = (g * l) % MOD
    with open(OUTPUT_FILE, 'a') as p:
        p.write(f"Case #{t + 1}: {(w - g) % MOD}\n")

with open(INPUT_FILE, 'r') as f:
    sys.stdin = f
    for i in range(int(input())):
        solve(i)
