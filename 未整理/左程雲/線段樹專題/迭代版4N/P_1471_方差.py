import sys
input = lambda: sys.stdin.readline().strip()
MII = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())

class SegTree:
    def __init__(self, init):
        self.n = len(init) if isinstance(init, list) else init
        m = 2 << self.n.bit_length()
        self.tr = [0] * m
        self.tr2 = [0] * m
        self.d = [0] * m
        if isinstance(init, list):
            self.build(init)
    
    def apply(self, i, l, r, val):
        n = r - l + 1
        self.tr2[i] += val ** 2 * n + 2 * self.tr[i] * val
        self.tr[i] += val * n
        self.d[i] += val
    
    def pull(self, i):
        self.tr[i] = self.tr[i << 1] + self.tr[i << 1 | 1]
        self.tr2[i] = self.tr2[i << 1] + self.tr2[i << 1 | 1]

    def push(self, i, l, r):
        if self.d[i]:
            m = (l + r) // 2
            self.apply(i << 1, l, m, self.d[i])
            self.apply(i << 1 | 1, m + 1, r, self.d[i])
            self.d[i] = 0
    
    def build(self, init):
        st = [(0, 1, 1, self.n)]
        while st:
            stat, i, l, r = st.pop()
            if stat == 0:
                if l == r:
                    self.tr[i] = init[l - 1]
                    self.tr2[i] = init[l - 1] ** 2
                    continue
                st.append((1, i, l, r))
                m = (l + r) // 2
                st.append((0, i << 1, l, m))
                st.append((0, i << 1 | 1, m + 1, r))
            else:
                self.pull(i)

    def add(self, s, e, val):
        st = [(0, 1, 1, self.n)]
        while st:
            stat, i, l, r = st.pop()
            if stat == 0:
                if s <= l and r <= e:
                    self.apply(i, l, r, val)
                    continue
                st.append((1, i, l, r))
                m = (l + r) // 2
                self.push(i, l, r)
                if s <= m: 
                    st.append((0, i << 1, l, m))
                if m < e: 
                    st.append((0, i << 1 | 1, m + 1, r))
            else:
                self.pull(i)
       
    def query(self, s, e):
        st = [(1, 1, self.n)]
        res1 = res2 = 0
        while st:
            i, l, r = st.pop()
            if s <= l and r <= e:
                res1 += self.tr[i]
                res2 += self.tr2[i]
                continue
            m = (l + r) // 2
            self.push(i, l, r)
            if s <= m: 
                st.append((i << 1, l, m))
            if m < e: 
                st.append((i << 1 | 1, m + 1, r))
        return res1, res2

def solve():
    tr = SegTree(a)
    for _ in range(m):
        q = tuple(input().split())  
        l, r = int(q[1]), int(q[2])
        if q[0] == '1': 
            k = float(q[3])
            tr.add(l, r, k)
        elif q[0] == '2':
            s = tr.query(l, r)[0]
            print(f'{s / (r - l + 1):.4f}')
        else:
            s, s2 = tr.query(l, r)
            n_ = (r - l + 1)
            mu = s / n_
            res = s2 / n_ - mu ** 2
            print(f'{res:.4f}')
               
for _ in range(1):
    n, m = MII()
    a = list(map(float, input().split()))
    solve()