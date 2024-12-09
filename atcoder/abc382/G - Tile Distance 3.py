import sys
import math

def compute_tile_indices(x, y, K):
    i = x // K
    j = y // K
    parity = (i + j) % 2
    if parity == 0:
        # Horizontal tile
        k = y - j * K
    else:
        # Vertical tile
        k = x - i * K
    return i, j, k

def solve():
    import sys
    import threading
    def main():
        T = int(sys.stdin.readline())
        for _ in range(T):
            K_str, Sx_str, Sy_str, Tx_str, Ty_str = sys.stdin.readline().split()
            K = int(K_str)
            Sx = int(Sx_str)
            Sy = int(Sy_str)
            Tx = int(Tx_str)
            Ty = int(Ty_str)

            # Adjust points by adding 0.5 as per problem statement
            Sx += 0.5
            Sy += 0.5
            Tx += 0.5
            Ty += 0.5

            # Convert to integer coordinates
            Sx = int(math.floor(Sx))
            Sy = int(math.floor(Sy))
            Tx = int(math.floor(Tx))
            Ty = int(math.floor(Ty))

            # Compute tile indices
            i_s = Sx // K
            j_s = Sy // K
            i_t = Tx // K
            j_t = Ty // K

            parity_s = (i_s + j_s) % 2
            parity_t = (i_t + j_t) % 2

            if parity_s == 0:
                k_s = Sy - j_s * K
            else:
                k_s = Sx - i_s * K

            if parity_t == 0:
                k_t = Ty - j_t * K
            else:
                k_t = Tx - i_t * K

            # Calculate minimum moves
            ans = abs(i_s - i_t) + abs(j_s - j_t) + abs(k_s - k_t)
            print(ans)
    threading.Thread(target=main).start()
solve()

