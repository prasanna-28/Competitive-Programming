import sys
from fractions import Fraction
from math import gcd

def esc(n, x, y, vx, vy):
    s = vy * (n - x) - vx * (n - y)
    if s % n or s // n % gcd(vx, vy):
        return -1                  

    px = Fraction(x)
    py = Fraction(y)
    a  = vx
    b  = vy
    hit = 0

    while True:
        t, typ = min(
            ((n - px - py) / (a + b), 'h') if a + b > 0 else (None, None),
            (px / -a, 'x') if a < 0 else (None, None),
            (py / -b, 'y') if b < 0 else (None, None),
            key=lambda z: z[0] if z[0] is not None else Fraction(10**99)
        )
        px += a * t
        py += b * t

        # which sides hit simultaneously?
        sides = []
        if a + b > 0 and (n - px - py) == 0: sides.append('h')
        if a < 0 and px == 0:               sides.append('x')
        if b < 0 and py == 0:               sides.append('y')

        # vertex?
        if ('x' in sides and 'y' in sides) or \
           ('h' in sides and len(sides) > 1):
            return hit

        hit += len(sides)

        if 'h' in sides:  a, b = -b, -a
        if 'x' in sides:  a = -a
        if 'y' in sides:  b = -b

def sol():
    it = iter(sys.stdin.read().split())
    tc = int(next(it))
    out = []
    for _ in range(tc):
        n = int(next(it)); x = int(next(it)); y = int(next(it))
        vx = int(next(it)); vy = int(next(it))
        out.append(str(esc(n, x, y, vx, vy)))
    sys.stdout.write('\n'.join(out))

if __name__ == "__main__":
    sol()

