import sys
def main():
    def can_assign(v, groups):
        robot1_pos = None
        robot1_time = None
        robot2_pos = None
        robot2_time = None

        for ti, c_list in groups:
            if len(c_list) ==1:
                ci = c_list[0]
                if robot1_pos is None or abs(ci - robot1_pos) <= v * (ti - robot1_time):
                    robot1_pos = ci
                    robot1_time = ti
                elif robot2_pos is None or abs(ci - robot2_pos) <= v * (ti - robot2_time):
                    robot2_pos = ci
                    robot2_time = ti
                else:
                    return False
            elif len(c_list) ==2:
                c1, c2 = c_list
                assign1 = (robot1_pos is None or abs(c1 - robot1_pos) <= v * (ti - robot1_time)) and \
                          (robot2_pos is None or abs(c2 - robot2_pos) <= v * (ti - robot2_time))
                assign2 = (robot1_pos is None or abs(c2 - robot1_pos) <= v * (ti - robot1_time)) and \
                          (robot2_pos is None or abs(c1 - robot2_pos) <= v * (ti - robot2_time))
                if assign1 and assign2:
                    if robot1_pos is None:
                        robot1_pos, robot1_time = c1, ti
                        robot2_pos, robot2_time = c2, ti
                    else:
                        move1 = abs(c1 - robot1_pos)
                        move2 = abs(c2 - robot1_pos)
                        if move1 <= move2:
                            robot1_pos, robot1_time = c1, ti
                            robot2_pos, robot2_time = c2, ti
                        else:
                            robot1_pos, robot1_time = c2, ti
                            robot2_pos, robot2_time = c1, ti
                elif assign1:
                    robot1_pos, robot1_time = c1, ti
                    robot2_pos, robot2_time = c2, ti
                elif assign2:
                    robot1_pos, robot1_time = c2, ti
                    robot2_pos, robot2_time = c1, ti
                else:
                    return False
            else:
                return False
        return True


    input = sys.stdin.read
    data = input().split()
    ptr =0
    T = int(data[ptr])
    ptr +=1
    for _ in range(T):
        if ptr >= len(data):
            break
        n = int(data[ptr])
        ptr +=1
        coins = []
        for _ in range(n):
            if ptr +1 >= len(data):
                break
            ti = int(data[ptr])
            ci = int(data[ptr+1])
            coins.append( (ti, ci) )
            ptr +=2
        groups = []
        if n >0:
            current_ti = coins[0][0]
            current_c = [coins[0][1]]
            for i in range(1, n):
                ti, ci = coins[i]
                if ti == current_ti:
                    current_c.append(ci)
                else:
                    groups.append( (current_ti, current_c) )
                    current_ti = ti
                    current_c = [ci]
            groups.append( (current_ti, current_c) )
        impossible = False
        for ti, c_list in groups:
            if len(c_list) > 2:
                impossible = True
                break
        if impossible:
            print(-1)
            continue
        left =0
        right = 10**9
        answer = -1
        while left <= right:
            mid = (left + right) //2
            if can_assign(mid, groups):
                answer = mid
                right = mid -1
            else:
                left = mid +1
        print(answer)

if __name__ == "__main__":
    main()




class SegmentTree:
    def __init__(self, length, neutral = INF, func = min, iter = True):
        self._size = 1
        self._iterative = iter
        self._neutral = neutral
        while self._size < length: self._size <<= 1
        self.arr = [self._neutral]*(self._size*2)
        self._func = func

    def __setitem__(self, idx, value):
        if self._iterative:
            self._iter_set(idx, value)
        else:
            self._set(idx, value, 0, 0, self._size)

    def __delitem__(self, idx):
        self[idx] = self._neutral

    def __getitem__(self, idx):
        return self.arr[self._size + idx - 1]

    def __len__(self):
        return len(self.arr)

    def __repr__(self):
        res = []
        x = 1
        l = 0
        while l < len(self.arr):
            curr = []
            for _ in range(x):
                curr.append(self.arr[l])
                l += 1
                if l >= len(self.arr): break
            else:
                res.append(ljoin(curr))
            x <<= 1
        return '\n'.join(res)

    def _op(self, a, b):
        return self._func(a,b)

    def _build(self, arr, x, lx, rx):
        if rx - lx == 1:
            if lx < len(arr):
                self.arr[x] = arr[lx]
            return
        m = (rx + lx)//2
        self._build( arr, 2*x + 1, lx, m)
        self._build( arr, 2*x + 2, m, rx)
        self.arr[x] = self._op(self.arr[2*x + 1], self.arr[2*x + 2])

    def build(self, arr):
        self._build(arr, 0, 0, self._size)

    def _set(self, i, v, x, lx, rx):
        if rx - lx <= 1:
            # leaf node
            self.arr[x] = v
            return

        m = (lx + rx) // 2
        if i < m:
            self._set(i, v, 2*x + 1, lx, m)
        else:
            self._set(i, v, 2*x + 2, m, rx)

        self.arr[x] = self._op(self.arr[2*x + 1], self.arr[2*x + 2])

    def _query(self, l, r, x, lx, rx):
        if lx >= r or l >= rx: return self._neutral
        if lx >= l and rx <= r: return self.arr[x]
        m = (lx + rx) // 2
        a1 = self._query(l, r, 2*x + 1, lx, m)
        a2 = self._query(l, r, 2*x + 2, m, rx)
        return self._op(a1, a2)

    def query(self, l, r):
        # l <= i < r
        if self._iterative:
            return self._iter_query(l, r - 1)
        return self._query(l, r, 0, 0, self._size)

    def _iter_query(self, l, r):
        v = self._neutral
        l += self._size
        r += self._size + 1
        while l < r:
            if l & 1:
                v = self._op(v, self.arr[l])
                l += 1
            if r & 1:
                r -= 1
                v = self._op(v, self.arr[r])
            l //= 2
            r //= 2
        return v

    def _iter_set(self, i, v):
        i += self._size
        self.arr[i] = v
        i //= 2
        while i > 0:
            left = self.arr[i * 2]
            right = self.arr[i * 2 + 1] if i * 2 + 1 < len(self.arr) else self._neutral
            self.arr[i] = self._op(left, right)
            i //= 2


