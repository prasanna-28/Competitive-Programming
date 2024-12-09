import math
import sys

limit = 10**7 + 1
sieve = [True] * limit
sieve[0:2] = [False, False]

for number in range(2, int(math.isqrt(limit)) + 1):
    if sieve[number]:
        sieve[number*number:limit:number] = [False] * len(range(number*number, limit, number))

primes = [num for num, is_prime in enumerate(sieve) if is_prime]

def solve(t):
    n = int(input())
    if n < 5:
        out = 0
    else:
        out = 1
        i = 1
        while i < len(primes) and primes[i] <= n:
            if primes[i] - primes[i - 1] == 2:
                out += 1
            i += 1
    with open("output.txt", 'a') as w:
        w.write(f"Case #{t +1 }: {out}\n")

FILE = "testcases/prime_subtractorization_input.txt"
with open(FILE, 'r') as f:
    sys.stdin = f
    for t in range(int(input())):
        solve(t)
