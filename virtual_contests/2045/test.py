import sys, math
from collections import deque, defaultdict, Counter

MOD       = 10**9 + 7
FASTIO    = False
DEBUG     = False
INF       = float('inf')
NINF      = float('-inf')
YES, NO   = "YES", "NO"
MT        = not True
B_MAX = 30
#====================Solution====================
def sol():
    n,m = ivars()
    A = list(map(lambda x: bin(x)[2:].zfill(B_MAX), ilist()))
    b = list(map(lambda x: bin(x)[2:].zfill(B_MAX), ilist()))
    res = 0
    c = Counter(b)
    b = list(set(b))

    for i in c:
        res += (c[i] * (c[i] - 1))//2

    a = list(A)
    if len(a) == 1:
        print(res)
        return
    trie_X = [-1, -1, 0]
    trie_A = [-1, -1, 0]
    depth = -1
    for x in a:
        node = 0
        trie_A[node * 3 + 2] += 1
        for idx, i in enumerate(x):
            i = int(i)
            if ~trie_A[node*3 + i]:
                node = trie_A[node*3 + i]
                trie_A[node*3 + 2] += 1
                if ~trie_A[node*3 + (i^1)]:
                    depth = max(depth, idx)
            else:
                if ~trie_A[node * 3 + (1 ^ i)]:
                    depth = max(depth, idx)
                new = [-1, -1, 1]
                trie_A[node*3 + i] = len(trie_A)//3
                trie_A.extend(new)
                node = len(trie_A)//3 - 1
    diffs = [depth]
    pairs = defaultdict(list)
    for i in a:
        pairs[i[:depth]].append(i)
    l = defaultdict(list)
    for k, v in pairs.items():
        if len(v) != 2:
            continue
        p1 = v.pop()
        p2 = v.pop()
        start = depth + 1
        d = 0
        for i in range(depth + 1, B_MAX):
            if p1[i] != p2[i]:
                l[d].append(i)
                d += 1
    prev = depth
    for d in sorted(l.keys()):
        curr = prev
        for i in l[d]:
            curr = max(curr, i)
        if curr == prev:
            break
        prev = curr
        diffs.append(curr)

    diffs = set(diffs)
    
    for x in b:
        node = 0
        for idx, i in enumerate(x):
            i = int(i)
            if idx in diffs:
                if ~trie_X[3 * node + i]:
                    res += trie_X[3*trie_X[3*node+i] + 2]
                if ~trie_X[node*3 + (i ^ 1)]:
                    node = trie_X[node*3 + (i^1)]
                else:
                    break
            else:
                if ~trie_X[node * 3 + i]:
                    node = trie_X[node*3 + i]
                else:
                    break

        node = 0
        trie_X[node * 3 + 2] += 1
        for i in x:
            i = int(i)
            if ~trie_X[node*3 + i]:
                node = trie_X[node*3 + i]
                trie_X[node*3 + 2] += 1
            else: 
                new = [-1, -1, 1]
                trie_X[node*3 + i] = len(trie_X)//3
                trie_X.extend(new)
                node = len(trie_X)//3 - 1

    print(res)




def sol_3():
    n,m = ivars()
    a = ilist()
    b = ilist()
    res = 0

    if len(set(a)) == 1:
        c = Counter(b)
        for i in c:
            res += (c[i] * (c[i] - 1))//2
        print(res)
        return

    trie_X = [-1, -1, 0]
    trie_A = [-1, -1, 0]

    for x in map(lambda x: bin(x)[2:].zfill(B_MAX), a):
        node = 0
        trie_A[node * 3 + 2] += 1
        for i in x:
            i = int(i)
            if ~trie_A[node*3 + i]:
                node = trie_A[node*3 + i]
                trie_A[node*3 + 2] += 1
            else:
                new = [-1, -1, 1]
                trie_A[node*3 + i] = len(trie_A)//3
                trie_A.extend(new)
                node = len(trie_A)//3 - 1

    for x in map(lambda x: bin(x)[2:].zfill(B_MAX), a):
        node = 0
        i = 0
        node = 0
        trie_X[node * 3 + 2] += 1
        for i in x:
            i = int(i)
            if ~trie_X[node*3 + i]:
                node = trie_X[node*3 + i]
                trie_X[node*3 + 2] += 1
            else: 
                new = [-1, -1, 1]
                trie_X[node*3 + i] = len(trie_X)//3
                trie_X.extend(new)
                node = len(trie_X)//3 - 1

    q = deque([(0, 0)])
    layers_X = defaultdict(list)
    layers_A = defaultdict(list)
    while q:
        index, layer = q.popleft()
        left, right = trie_A[index * 3], trie_A[index * 3 + 1]
        if ~left:
            layers_A[layer].append(trie_A[left * 3 + 2])
            q.append((left, layer + 1))
        else:
            layers_A[layer].append(0)
        if ~right:
            layers_A[layer].append(trie_A[right * 3 + 2])
            q.append((right, layer + 1))
        else:
            layers_A[layer].append(0)

    q = deque([(0, 0)])
    while q:
        index, layer = q.popleft()
        left, right = trie_X[index * 3], trie_X[index * 3 + 1]
        if ~left:
            layers_X[layer].append(trie_X[left * 3 + 2])
            q.append((left, layer + 1))
        else:
            layers_X[layer].append(0)
        if ~right:
            layers_X[layer].append(trie_X[right * 3 + 2])
            q.append((right, layer + 1))
        else:
            layers_A[layer].append(0)
    
    for layer in range(B_MAX):
        layer_A = layers_A[layer]
        layer_X = layers_X[layer]
        if max(layer_A) <= 1:
            for i in layer_X:
                res += (i * (i - 1))//2

    print(res)

def sol_4():
    n,m = ivars()
    A = list(map(lambda x: bin(x)[2:].zfill(B_MAX), ilist()))
    b = list(map(lambda x: bin(x)[2:].zfill(B_MAX), ilist()))
    res = 0
    c = Counter(b)
    b = list(set(b))

    for i in c:
        res += (c[i] * (c[i] - 1))//2

    a = list(set(A))
    if len(a) != len(A):
        print(res)
        return
    trie_X = [-1, -1, 0]
    trie_A = [-1, -1, 0]
    depth = -1
    for x in a:
        node = 0
        trie_A[node * 3 + 2] += 1
        for idx, i in enumerate(x):
            i = int(i)
            if ~trie_A[node*3 + i]:
                node = trie_A[node*3 + i]
                trie_A[node*3 + 2] += 1
                if ~trie_A[node*3 + (i^1)]:
                    depth = max(depth, idx)
            else:
                if ~trie_A[node * 3 + (1 ^ i)]:
                    depth = max(depth, idx)
                new = [-1, -1, 1]
                trie_A[node*3 + i] = len(trie_A)//3
                trie_A.extend(new)
                node = len(trie_A)//3 - 1
    diffs = [depth]
    pairs = defaultdict(list)
    for i in a:
        pairs[i[:depth]].append(i)
    candidates = defaultdict(int)
    for i in pairs:
        if len(pairs[i]) == 2:
            p1 = pairs[i].pop()
            p2 = pairs[i].pop()
            curridx = diffs[-1] + 1
            while curridx < B_MAX and (p1[curridx] == p2[curridx]):
                curridx += 1
            candidates[(p1, p2)] = curridx
    while len(candidates.keys()):
        curr = max(candidates.values())
        diffs.append(curr)
        delete = []
        for i,v in candidates.items():
            if v < curr:
                delete.append(i)
        
        while delete:
            del candidates[delete.pop()]

        for (p1, p2) in candidates.keys():
            value = candidates[(p1, p2)] + 1
            while value < B_MAX and p1[value] == p2[value]:
                value += 1
            if value == B_MAX:
                delete.append((p1, p2))
            else:
                candidates[(p1, p2)] = value

        while delete:
            del candidates[delete.pop()]
    diffs = set(diffs)
    
    for x in b:
        node = 0
        for idx, i in enumerate(x):
            i = int(i)
            if idx in diffs:
                if ~trie_X[3 * node + i]:
                    res += trie_X[3*trie_X[3*node+i] + 2]
                if ~trie_X[node*3 + (i ^ 1)]:
                    node = trie_X[node*3 + (i^1)]
                else:
                    break
            else:
                if ~trie_X[node * 3 + i]:
                    node = trie_X[node*3 + i]
                else:
                    break

        node = 0
        trie_X[node * 3 + 2] += 1
        for i in x:
            i = int(i)
            if ~trie_X[node*3 + i]:
                node = trie_X[node*3 + i]
                trie_X[node*3 + 2] += 1
            else: 
                new = [-1, -1, 1]
                trie_X[node*3 + i] = len(trie_X)//3
                trie_X.extend(new)
                node = len(trie_X)//3 - 1

    print(res)

def sol_1():
    n, m = ivars()
    a = ilist()
    b = ilist()
    root = [-1, -1]
    trie = [root]
    for i in a:
        i = bin(i)[2:].zfill(B_MAX)
        print(i)
        node = root
        for bit in map(int, i):
            if ~node[bit]:
                node = trie[node[bit]]
            else:
                node[bit] = len(trie)
                node = [-1, -1]
                trie.append(node)

    q = deque([[root, 0]])
    need = set()
    while q:
        [left, right], layer = q.popleft()
        if ~left and ~right:
            need.add(layer)
        if ~left:
            q.append([trie[left], layer + 1])
        if ~right:
            q.append([trie[right], layer + 1])

    d = defaultdict(int)
    res = 0
    print(need)
    for x in b:
        x, x_, x__= bin(x)[2:].zfill(B_MAX), [], []
        for i in range(B_MAX):
            if i in need:
                x_.append(x[i])
                x__.append(str(int(x[i]) ^ 1))
        res += d[''.join(x_)]
        d[''.join(x_)] += 1
    for i, v in d.items():
        print(i, v)
    print(res)


'''
00000
00111
01101
10110
11000

01100
01010
'''

#================================================

def main():
    for _ in range(ipt() if MT else 1):
        sol()


def debug(*args):
    if DEBUG:
        for arg in args:
            print(arg)

def ASSERT(cond):
    if DEBUG:
        assert(cond)


if FASTIO:
    import os
    from io import BytesIO, IOBase

    _str = str
    str = lambda x=b"": x if type(x) is bytes else _str(x).encode()

    BUFSIZE = 8192


    class FastIO(IOBase):
        newlines = 0

        def __init__(self, file):
            self._file = file
            self._fd = file.fileno()
            self.buffer = BytesIO()
            self.writable = "x" in file.mode or "r" not in file.mode
            self.write = self.buffer.write if self.writable else None

        def read(self):
            while True:
                b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
                if not b:
                    break
                ptr = self.buffer.tell()
                self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
            self.newlines = 0
            return self.buffer.read()

        def readline(self):
            while self.newlines == 0:
                b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
                self.newlines = b.count(b"\n") + (not b)
                ptr = self.buffer.tell()
                self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
            self.newlines -= 1
            return self.buffer.readline()

        def flush(self):
            if self.writable:
                os.write(self._fd, self.buffer.getvalue())
                self.buffer.truncate(0), self.buffer.seek(0)


    class IOWrapper(IOBase):
        def __init__(self, file):
            self.buffer = FastIO(file)
            self.flush = self.buffer.flush
            self.writable = self.buffer.writable
            self.write = lambda s: self.buffer.write(s.encode("ascii"))
            self.read = lambda: self.buffer.read().decode("ascii")
            self.readline = lambda: self.buffer.readline().decode("ascii")


    sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
    input = lambda: sys.stdin.readline().rstrip("\r\n")

if __name__ == "__main__":
    finp        = sys.stdin.readline
    njoin       = lambda x: '\n'.join(map(str, x))
    ljoin       = lambda x: ' '.join(map(str, x))
    sjoin       = lambda x: '\n'.join(x)
    ilist       = lambda: list(map(int, finp().split()))
    slist       = lambda: list(input())
    slists      = lambda: input().split()
    ivars       = lambda: map(int, finp().split())
    ipt         = lambda: int(finp())
    main()


