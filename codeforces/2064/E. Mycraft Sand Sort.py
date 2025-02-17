MOD = 998244353

def solve():
    import sys
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    t = int(input_data[0])
    index = 1
    out_lines = []
    for _ in range(t):
        n = int(input_data[index])
        index += 1
        # Read p but note: we do not use it in this implementation.
        p = list(map(int, input_data[index:index+n]))
        index += n
        # Read c – the colours array.
        c = list(map(int, input_data[index:index+n]))
        index += n

        # Precompute factorials up to n.
        fact = [1] * (n+1)
        for i in range(2, n+1):
            fact[i] = fact[i-1] * i % MOD

        # 1. Compute the local score:
        # For each contiguous block (segment) of same colour, multiply by factorial(length).
        local_score = 1
        i = 0
        while i < n:
            j = i
            while j < n and c[j] == c[i]:
                j += 1
            seg_len = j - i
            local_score = local_score * fact[seg_len] % MOD
            i = j

        # 2. Compute the global score:
        # We use a monotonic stack. For each new block we “look backwards” for a block with the same colour.
        global_score = 1
        stack = []
        for i in range(n):
            # Pop from stack while the top has a colour less than c[i].
            while stack and c[stack[-1]] < c[i]:
                stack.pop()
            if stack and c[stack[-1]] == c[i]:
                # We have found an earlier block of the same colour that is not in the same contiguous segment.
                gap = i - stack[-1] - 1
                global_score = global_score * (gap + 1) % MOD
                # Replace the top with the current index (so that future gaps are measured from here).
                stack[-1] = i
            else:
                stack.append(i)

        # The final answer is the product of the two contributions modulo MOD.
        ans = local_score * global_score % MOD
        out_lines.append(str(ans))
    sys.stdout.write("\n".join(out_lines))

if __name__ == '__main__':
    solve()

