import sys
input = lambda: sys.stdin.readline().strip()
MII = lambda: map(int, input().split())

class SegTree:
    def __init__(self, init):
        self.n = len(init)
        m = 2 << self.n.bit_length()
        self.len = [0] * m
        self.times = [0] * m
        self.cover = [0] * m
        self.build(init)
    
    def pull(self, order):
        for i in reversed(order):
            if self.times[i] > 0:
                self.cover[i] = self.len[i]
            else:
                l, r = i << 1, i << 1 | 1
                self.cover[i] = 0
                if l < len(self.cover):
                    self.cover[i] += self.cover[l]
                if r < len(self.cover):
                    self.cover[i] += self.cover[r]
    
    def build(self, init):
        st = [(1, 0, self.n - 1)]
        while st:
            i, l, r = st.pop()
            if r < self.n - 1:
                self.len[i] = init[r + 1] - init[l]
            if l == r:
                continue
            m = (l + r) >> 1
            st.append((i << 1, l, m))
            st.append((i << 1 | 1, m + 1, r))
    
    def update(self, s, e, cnt):
        st = [(1, 0, self.n - 1)]
        order = []
        while st:
            i, l, r = st.pop()
            if s <= l and r <= e:
                self.times[i] += cnt
            else:
                m = (l + r) >> 1
                if s <= m: st.append((i << 1, l, m))
                if m < e: st.append((i << 1 | 1, m + 1, r))
            order.append(i) # 都要up?
        self.pull(order)
    
def solve():
    m = set()
    lines = [] # x = 10, y = 10 ~ 20, +1...
    for x1, y1, x2, y2 in a:
        m.update([y1, y2])
        lines.append([x1, y1, y2, 1])
        lines.append([x2, y1, y2, -1])
    m = {x: i for i, x in enumerate(sorted(m))} 
    tr = SegTree(list(m.keys()))
    lines.sort()
    
    ans = preX = 0 # tr.cover[1]一開始為0，無須初始化
    for x, y1, y2, cnt in lines:
        ans += tr.cover[1] * (x - preX) 
        preX = x
        l, r = m[y1], m[y2]
        tr.update(l, r - 1, cnt)
    print(ans)
        
for _ in range(1):
    n = int(input())
    a = [tuple(MII()) for _ in range(n)]
    solve()