import sys
input = lambda: sys.stdin.readline().strip()
MII = lambda: map(int, input().split())
class SegTree:
    def __init__(self, init):
        self.n = len(init)
        self.tr = [0] * (self.n * 2)
        self.d = [0] * (self.n * 2)
        self.build(init)
    
    def apply(self, i, l, r, val):
        self.tr[i] += val * (r - l + 1)
        self.d[i] += val
    
    def pull(self, order):
        for i, ln in reversed(order):
            self.tr[i] = self.tr[i + 1] + self.tr[i + ln * 2]
    
    def push(self, i, l, r):
        if self.d[i]:
            m = (l + r) >> 1
            ln = m - l + 1
            self.apply(i + 1, l, m, self.d[i])
            self.apply(i + ln * 2, m + 1, r, self.d[i])
            self.d[i] = 0
    
    def build(self, init):
        st = [(0, 1, self.n)]
        order = []
        while st:
            i, l, r = st.pop()
            if l == r:
                self.tr[i] = init[l - 1]
                continue
            m = (l + r) >> 1
            ln = m - l + 1
            st.append((i + 1, l, m))
            st.append((i + ln * 2, m + 1, r))
            order.append((i, ln))
        self.pull(order)
    
    def add(self, s, e, val):
        st = [(0, 1, self.n)]
        order = []
        while st:
            i, l, r = st.pop()
            if s <= l and r <= e:
                self.apply(i, l, r, val)
                continue
            self.push(i, l, r)
            m = (l + r) >> 1
            ln = m - l + 1
            if s <= m: st.append((i + 1, l, m))
            if m < e: st.append((i + ln * 2, m + 1, r))
            order.append((i, ln))
        self.pull(order)
    
    def query(self, s, e):
        st = [(0, 1, self.n)]
        res = 0
        while st:
            i, l, r = st.pop()
            if s <= l and r <= e:
                res += self.tr[i]
                continue
            self.push(i, l, r)
            m = (l + r) >> 1
            ln = m - l + 1
            if s <= m: st.append((i + 1, l, m))
            if m < e: st.append((i + ln * 2, m + 1, r))
        return res

def solve():
    tr = SegTree(a)
    for _ in range(m):
        q = tuple(MII())
        if q[0] == 1:
            tr.add(q[1], q[2], q[3])
        else:
            print(tr.query(q[1], q[2])) 
               
for _ in range(1):
    n, m = MII()
    a = list(MII())
    solve()