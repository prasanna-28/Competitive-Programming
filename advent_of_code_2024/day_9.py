def main():
    s = list(map(int,list(input())))
    odds = []
    evens = []
    for i in range(len(s)):
        if i & 1:
            odds.append(s[i])
        else:
            evens.append((i//2, s[i]))
    fillers = [[] for _ in range(len(odds))]
    st = SegmentTree([(odds[i], i) for i in range(len(odds))])
    newevens = [-1] * len(evens)
    for j in range(len(evens) - 1, -1, -1):
        result = -1
        l = 0
        r = len(odds)
        while l < r:
            mid = (r + l)//2
            k = st.query(0, mid)
            if k[0] >= evens[j][1]:
                result = k[1]
                r = mid
            else:
                l = mid + 1
        if result == -1 or result >= j:
            newevens[j] = evens[j]
        else:
            fillers[result].append(evens[j])
            st[result] = (st[result][0] - evens[j][1], result)
            if j > 0:
                st[j - 1] = (st[j - 1][0] + evens[j][1], j - 1)
    index = 0
    checksum = 0

    for i in range(len(s)):
        if i & 1:
            i = i//2
            for v, ct in fillers[i]:
                while ct > 0:
                    checksum += index * v
                    index += 1
                    ct -= 1
            index += st[i][0]
        else:
            i = i//2
            if newevens[i] == -1:
                continue
            else:
                newevens[i] = list(newevens[i])
                while newevens[i][1] > 0:
                    newevens[i][1] -= 1
                    checksum += newevens[i][0] * index
                    index += 1
    print(checksum)


class SegmentTree:
    def __init__(self, data, default=(-1, -1), func=max):
        """initialize the segment tree with data"""
        self._default = default
        self._func = func
        self._len = len(data)
        self._size = _size = 1 << (self._len - 1).bit_length()

        self.data = [default] * (2 * _size)
        self.data[_size:_size + self._len] = data
        for i in reversed(range(_size)):
            self.data[i] = func(self.data[i + i], self.data[i + i + 1])

    def __delitem__(self, idx):
        self[idx] = self._default

    def __getitem__(self, idx):
        return self.data[idx + self._size]

    def __setitem__(self, idx, value):
        idx += self._size
        self.data[idx] = value
        idx >>= 1
        while idx:
            self.data[idx] = self._func(self.data[2 * idx], self.data[2 * idx + 1])
            idx >>= 1

    def __len__(self):
        return self._len

    def query(self, start, stop):
        """func of data[start, stop)"""
        start += self._size
        stop += self._size

        res_left = res_right = self._default
        while start < stop:
            if start & 1:
                res_left = self._func(res_left, self.data[start])
                start += 1
            if stop & 1:
                stop -= 1
                res_right = self._func(self.data[stop], res_right)
            start >>= 1
            stop >>= 1

        return self._func(res_left, res_right)

    def __repr__(self):
        return "SegmentTree({0})".format(self.data)
main()


