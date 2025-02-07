import sys
input = lambda: sys.stdin.readline().strip()
MII = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())

class SegTree:
    def __init__(self, init):
        self.n = len(init) if isinstance(init, list) else init
        m = 2 << self.n.bit_length()
        self.tr = [0] * m
        self.rev = [False] * m
        if isinstance(init, list):
            self.build(init)
    
    def apply(self, i, l, r):
        n = r - l + 1
        self.tr[i] = n - self.tr[i]
        self.rev[i] ^= True
    
    def pull(self, i):
        self.tr[i] = self.tr[i << 1] + self.tr[i << 1 | 1]

    def push(self, i, l, r):
        if self.rev[i]:
            m = (l + r) // 2
            self.apply(i << 1, l, m)
            self.apply(i << 1 | 1, m + 1, r)
            self.rev[i] = False
    
    def build(self, init):
        st = [(0, 1, 1, self.n)]
        while st:
            stat, i, l, r = st.pop()
            if stat == 0:
                if l == r:
                    self.tr[i] = init[l - 1]
                    continue
                st.append((1, i, l, r))
                m = (l + r) // 2
                st.append((0, i << 1, l, m))
                st.append((0, i << 1 | 1, m + 1, r))
            else:
                self.pull(i)

    def reverse(self, s, e):
        st = [(0, 1, 1, self.n)]
        while st:
            stat, i, l, r = st.pop()
            if stat == 0:
                if s <= l and r <= e:
                    self.apply(i, l, r)
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
        res = 0
        while st:
            i, l, r = st.pop()
            if s <= l and r <= e:
                res += self.tr[i]
                continue
            m = (l + r) // 2
            self.push(i, l, r)
            if s <= m: 
                st.append((i << 1, l, m))
            if m < e: 
                st.append((i << 1 | 1, m + 1, r))
        return res

def solve():
    tr = SegTree(n)
    for _ in range(m):
        c, a, b = MII()
        if c == 0:
            tr.reverse(a, b)
        else:
            print(tr.query(a, b))
               
for _ in range(1):
    n, m = MII()
    solve()
