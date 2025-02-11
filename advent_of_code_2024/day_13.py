import sys
import re
import math

button_a_pattern = re.compile(r'Button A:\s*X\+(\d+),\s*Y\+(\d+)', re.IGNORECASE)
button_b_pattern = re.compile(r'Button B:\s*X\+(\d+),\s*Y\+(\d+)', re.IGNORECASE)
prize_pattern = re.compile(r'Prize:\s*X=(\d+),\s*Y=(\d+)', re.IGNORECASE)

def parse_line(line, pattern):
    match = pattern.match(line)
    return int(match.group(1)), int(match.group(2))

def main():
    total = 0
    while True:
        try:
            line_a = sys.stdin.readline()
            if not line_a:
                break
            line_a = line_a.strip()
            if not line_a:
                continue
            ax, ay = parse_line(line_a, button_a_pattern)

            line_b = sys.stdin.readline()
            if not line_b:
                break
            line_b = line_b.strip()
            bx, by = parse_line(line_b, button_b_pattern)

            line_p = sys.stdin.readline()
            if not line_p:
                break
            line_p = line_p.strip()
            px, py = parse_line(line_p, prize_pattern)
            px += 10000000000000
            py += 10000000000000
            if px % (math.gcd(ax, bx)) != 0:
                continue
            if py % (math.gcd(ay, by)) != 0:
                continue
            # i(ax) + j(bx) = px
            # i(ay) + j(by) = px
            copy = [ax, ay, bx, by, px, py]
            ax *= ay
            bx *= ay
            px *= ay
            ay *= copy[0]
            by *= copy[0]
            py *= copy[0]
            bx -= by
            px -= py
            if px % bx != 0:
                continue
            sol_j = px//bx
            py = copy[-1]
            ay = copy[1]
            by = copy[3]
            by *= sol_j
            py -= by
            if py % ay != 0:
                continue
            sol_i = py//ay
            if min(sol_i, sol_j) < 0:
                continue
            total += 3 * sol_i + sol_j
            print(total)
        except:
            print(total)
            continue


main()
