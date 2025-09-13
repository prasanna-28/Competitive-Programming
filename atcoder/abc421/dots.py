from collections import defaultdict

class DotsAndBoxes():
    def __init__(self):
        self.grid = defaultdict(int)
        self.seen = set()
    def incr(self, x, y):
        self.grid[(x, y)] += 1
        if self.grid[(x, y)] == 4:
            return True
        return False
    def insertLine(self, x1, y1, x2, y2):
        if (x1, y1, x2, y2) in self.seen or (x2, y2, x1, y1) in self.seen:
            return False
        self.seen.add((x1, y1, x2, y2))
        if x1 == x2:
            if self.incr(x1, y2):
                return True
            if self.incr(x1 + 1, y2):
                return True
        if y1 == y2:
            if self.incr(x2, y2):
                return True
            if self.incr(x2, y2+1):
                return True
        return False
