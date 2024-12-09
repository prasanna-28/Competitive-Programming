import sys
import threading

def main():
    import sys

    import sys

    t = int(sys.stdin.readline())
    for _ in range(t):
        line = ''
        while line.strip() == '':
            line = sys.stdin.readline()
        n = int(line.strip())
        s1 = ''
        while len(s1) < n:
            s1 += sys.stdin.readline().strip()
        s2 = ''
        while len(s2) < n:
            s2 += sys.stdin.readline().strip()
        # Precompute A's in each cell
        A1 = [1 if c == 'A' else 0 for c in s1]
        A2 = [1 if c == 'A' else 0 for c in s2]
        # Initialize DP
        dp_prev = [-1] * 3
        dp_prev[0] = 0
        for j in range(n):
            dp_next = [-1] *3
            for s in range(3):
                if dp_prev[s] == -1:
                    continue
                if s ==0:
                    if j+1 <n:
                        # Pattern 1: (0,j), (1,j), (0,j+1)
                        sum_A = A1[j] + A2[j] + A1[j+1]
                        vote = 1 if sum_A >=2 else 0
                        s_prime =2
                        if dp_next[s_prime] < dp_prev[s] + vote:
                            dp_next[s_prime] = dp_prev[s] + vote
                        # Pattern 2: (0,j), (1,j), (1,j+1)
                        sum_A = A1[j] + A2[j] + A2[j+1]
                        vote =1 if sum_A >=2 else 0
                        s_prime =1
                        if dp_next[s_prime] < dp_prev[s] + vote:
                            dp_next[s_prime] = dp_prev[s] + vote
                        # Pattern 3: (0,j), (0,j+1), (1,j+1)
                        sum_A = A1[j] + A1[j+1] + A2[j+1]
                        vote =1 if sum_A >=2 else 0
                        s_prime =0
                        if dp_next[s_prime] < dp_prev[s] + vote:
                            dp_next[s_prime] = dp_prev[s] + vote
                        # Pattern 4: (1,j), (0,j+1), (1,j+1)
                        sum_A = A2[j] + A1[j+1] + A2[j+1]
                        vote =1 if sum_A >=2 else 0
                        s_prime =0
                        if dp_next[s_prime] < dp_prev[s] + vote:
                            dp_next[s_prime] = dp_prev[s] + vote
                elif s ==1:
                    if j+1 <n:
                        # Place district: (1,j), (0,j+1), (1,j+1)
                        sum_A = A2[j] + A1[j+1] + A2[j+1]
                        vote =1 if sum_A >=2 else 0
                        s_prime =0
                        if dp_next[s_prime] < dp_prev[s] + vote:
                            dp_next[s_prime] = dp_prev[s] + vote
                elif s ==2:
                    if j+1 <n:
                        # Place district: (0,j), (0,j+1), (1,j+1)
                        sum_A = A1[j] + A1[j+1] + A2[j+1]
                        vote =1 if sum_A >=2 else 0
                        s_prime =0
                        if dp_next[s_prime] < dp_prev[s] + vote:
                            dp_next[s_prime] = dp_prev[s] + vote
            dp_prev = dp_next
        # After all columns, the residual state must be 0
        print(dp_prev)
        print(dp_prev[0] if dp_prev[0] != -1 else 0)

threading.Thread(target=main).start()

