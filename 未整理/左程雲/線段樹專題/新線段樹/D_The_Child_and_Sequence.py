import sys
input = lambda: sys.stdin.readline().strip()
MII = lambda: map(int, input().split())
class SegTree:
    def __init__(self, init):
        self.n = len(init)
        m = 2 << self.n.bit_length()
        self.tr1 = [0] * m
        self.tr2 = [0] * m
        self.build(init)
    
    def pull(self, order):
        for i in reversed(order):
            self.tr1[i] = self.tr1[i << 1] + self.tr1[i << 1 | 1]
            self.tr2[i] = max(self.tr2[i << 1], self.tr2[i << 1 | 1])
    
    def build(self, init):
        st = [(1, 1, self.n)]
        order = []
        while st:
            i, l, r = st.pop()
            if l == r:
                self.tr1[i] = self.tr2[i] = init[l - 1]
                continue
            m = (l + r) >> 1
            st.append((i << 1, l, m))
            st.append((i << 1 | 1, m + 1, r))
            order.append(i)
        self.pull(order)
    
    def mod(self, s, e, x):
        st = [(1, 1, self.n)]
        order = []
        while st:
            i, l, r = st.pop()
            if l == r:
                self.tr1[i] %= x
                self.tr2[i] %= x
                continue
            if self.tr2[i] < x:
                continue
            m = (l + r) >> 1
            if s <= m: st.append((i << 1, l, m))
            if m < e: st.append((i << 1 | 1, m + 1, r))
            order.append(i)
        self.pull(order)
    
    def set(self, u, val):
        st = [(1, 1, self.n)]
        order = []
        while st:
            i, l, r = st.pop()
            if l == r:
                self.tr1[i] = self.tr2[i] = val
                continue
            m = (l + r) >> 1
            if u <= m: st.append((i << 1, l, m))
            if m < u: st.append((i << 1 | 1, m + 1, r))
            order.append(i)
        self.pull(order)
    
    def query(self, s, e):
        st = [(1, 1, self.n)]
        res = 0
        while st:
            i, l, r = st.pop()
            if s <= l and r <= e:
                res += self.tr1[i]
                continue
            m = (l + r) >> 1
            if s <= m: st.append((i << 1, l, m))
            if m < e: st.append((i << 1 | 1, m + 1, r))
        return res

def solve():
    tr = SegTree(a)
    for _ in range(m):
        q = tuple(MII())
        if q[0] == 1:
            print(tr.query(q[1], q[2]))
        elif q[0] == 2:
            tr.mod(q[1], q[2], q[3])
        else:
            tr.set(q[1], q[2])
                   
for _ in range(1):
    n, m = MII()
    a = list(MII())
    solve()