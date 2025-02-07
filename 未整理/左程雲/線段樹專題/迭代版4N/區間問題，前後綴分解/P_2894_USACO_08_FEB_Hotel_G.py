import sys
input = lambda: sys.stdin.readline().strip()
MII = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())

class SegTree:
    def __init__(self, init):
        self.n = len(init) if isinstance(init, list) else init
        m = 2 << self.n.bit_length()
        self.len, self.pre, self.suf = [0] * m, [0] * m, [0] * m
        self.upd = [None] * m
        self.build()
    
    def apply(self, i, n, val):
        self.len[i] = self.pre[i] = self.suf[i] = n * int(val == 'Out')
        self.upd[i] = val
    
    def pull(self, i, ln, rn):
        l, r = i << 1, i << 1 | 1
        self.len[i] = max(self.len[l], self.len[r], self.suf[l] + self.pre[r])
        self.pre[i] = self.pre[l] + self.pre[r] * int(self.pre[l] == ln)
        self.suf[i] = self.suf[r] + self.suf[l] * int(self.suf[r] == rn)

    def push(self, i, ln, rn):
        if self.upd[i] is not None: # 先修改再增加
            self.apply(i << 1, ln, self.upd[i])
            self.apply(i << 1 | 1, rn, self.upd[i])
            self.upd[i] = None
    
    def build(self):
        st = [(0, 1, 1, self.n)]
        while st:
            stat, i, l, r = st.pop()
            m = (l + r) // 2
            ln, rn = m - l + 1, r - m
            if stat == 0:
                if l == r:
                    self.len[i] = self.pre[i] = self.suf[i] = 1
                    continue
                st.append((1, i, l, r))
                st.append((0, i << 1, l, m))
                st.append((0, i << 1 | 1, m + 1, r))
            else:
                self.pull(i, ln, rn)

    def modify(self, s, e, val):
        st = [(0, 1, 1, self.n)]
        while st:
            stat, i, l, r = st.pop()
            m = (l + r) // 2
            ln, rn = m - l + 1, r - m
            if stat == 0:
                if s <= l and r <= e:
                    self.apply(i, r - l + 1, val)
                    continue
                self.push(i, ln, rn)
                st.append((1, i, l, r))
                if s <= m: 
                    st.append((0, i << 1, l, m))
                if m < e: 
                    st.append((0, i << 1 | 1, m + 1, r))
            else:
                self.pull(i, ln, rn)
    
    def queryLeft(self, x): # 找左側連續長度>=x之index
        st = [(1, 1, self.n)]
        while st: # 無修改數組，不用特別紀錄順序，可直接return
            i, l, r = st.pop()
            if l == r:
                return l
            m = (l + r) // 2
            ln, rn = m - l + 1, r - m
            self.push(i, ln, rn) # 查子樹之前必須先push
            ls, rs = i << 1, i << 1 | 1
            if x <= self.len[ls]: # 最先查左边
                st.append((ls, l, m))
            else:
                if self.suf[ls] + self.pre[rs] >= x: # 中間
                    return m - self.suf[ls] + 1
                else:
                    st.append((rs, m + 1, r)) # 右邊

def solve():
    tr = SegTree(n)
    for _ in range(m):
        q = tuple(MII())
        if q[0] == 1:
            if tr.len[1] < q[1]: # root不用push更新，一定最大
                print(0)
            else:
                l = tr.queryLeft(q[1])
                tr.modify(l, min(l + q[1] - 1, n), 'In')
                print(l)
        else:
            tr.modify(q[1], min(q[1] + q[2] - 1, n), 'Out')        
                   
for _ in range(1):
    n, m = MII()
    solve()