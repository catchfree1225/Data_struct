import sys
input = lambda: sys.stdin.readline().strip()
MII = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())

class SegTree:
    def __init__(self, init):
        self.n = len(init) if isinstance(init, list) else init
        m = 2 << self.n.bit_length()
        self.tr = [0] * m
        self.len0, self.pre0, self.suf0 = [0] * m, [0] * m, [0] * m
        self.len1, self.pre1, self.suf1 = [0] * m, [0] * m, [0] * m
        self.upd = [None] * m
        self.rev = [False] * m 
        if isinstance(init, list):
            self.build(init)
    
    def apply(self, i, n, type, val=None):
        if type == 'upd':
            self.tr[i] = val * n
            self.len0[i] = self.pre0[i] = self.suf0[i] = n * int(val == 0)
            self.len1[i] = self.pre1[i] = self.suf1[i] = n * int(val == 1)
            self.upd[i] = val
            self.rev[i] = False # 取消其他操作
        if type == 'rev':
            self.tr[i] = n - self.tr[i]
            self.len0[i], self.len1[i] = self.len1[i], self.len0[i]
            self.pre0[i], self.pre1[i] = self.pre1[i], self.pre0[i]
            self.suf0[i], self.suf1[i] = self.suf1[i], self.suf0[i]
            self.rev[i] ^= True
    
    def pull(self, i, ln, rn):
        l, r = i << 1, i << 1 | 1
        self.tr[i] = self.tr[l] + self.tr[r]
        self.len0[i] = max(self.len0[l], self.len0[r], self.suf0[l] + self.pre0[r])
        self.pre0[i] = self.pre0[l] + self.pre0[r] * int(self.pre0[l] == ln)
        self.suf0[i] = self.suf0[r] + self.suf0[l] * int(self.suf0[r] == rn)
        self.len1[i] = max(self.len1[l], self.len1[r], self.suf1[l] + self.pre1[r])
        self.pre1[i] = self.pre1[l] + self.pre1[r] * int(self.pre1[l] == ln)
        self.suf1[i] = self.suf1[r] + self.suf1[l] * int(self.suf1[r] == rn)

    def push(self, i, ln, rn):
        if self.upd[i] is not None: # 先修改再增加
            self.apply(i << 1, ln, 'upd', self.upd[i])
            self.apply(i << 1 | 1, rn, 'upd', self.upd[i])
            self.upd[i] = None
        if self.rev[i]:
            self.apply(i << 1, ln, 'rev')
            self.apply(i << 1 | 1, rn, 'rev')
            self.rev[i] = False
    
    def build(self, init):
        st = [(0, 1, 1, self.n)]
        while st:
            stat, i, l, r = st.pop()
            m = (l + r) // 2
            ln, rn = m - l + 1, r - m
            if stat == 0:
                if l == r:
                    self.tr[i] = init[l - 1]
                    self.len0[i] = self.pre0[i] = self.suf0[i] = int(init[l - 1] == 0)
                    self.len1[i] = self.pre1[i] = self.suf1[i] = int(init[l - 1] == 1)
                    continue
                st.append((1, i, l, r))
                st.append((0, i << 1, l, m))
                st.append((0, i << 1 | 1, m + 1, r))
            else:
                self.pull(i, ln, rn)

    def modify(self, s, e, type, val=None):
        st = [(0, 1, 1, self.n)]
        while st:
            stat, i, l, r = st.pop()
            m = (l + r) // 2
            ln, rn = m - l + 1, r - m
            if stat == 0:
                if s <= l and r <= e:
                    self.apply(i, r - l + 1, type, val)
                    continue
                self.push(i, ln, rn)
                st.append((1, i, l, r))
                if s <= m: 
                    st.append((0, i << 1, l, m))
                if m < e: 
                    st.append((0, i << 1 | 1, m + 1, r))
            else:
                self.pull(i, ln, rn)
    
    def query_len(self, s, e):
        st = [(0, 1, 1, self.n)]
        info = {}
        while st:
            stat, i, l, r = st.pop()
            m = (l + r) // 2
            if stat == 0:
                if s <= l and r <= e:
                    info[i] = (self.len1[i], self.pre1[i], self.suf1[i])
                    continue
                ln, rn = m - l + 1, r - m
                self.push(i, ln, rn)
                st.append((1, i, l, r))
                if s <= m:
                    st.append((0, i << 1, l, m))
                if m < e:
                    st.append((0, i << 1 | 1, m + 1, r))
            else:
                llen, lpre, lsuf = info.get(i << 1, (0, 0, 0))
                rlen, rpre, rsuf = info.get(i << 1 | 1, (0, 0, 0))
                ln, rn = m - max(l, s) + 1, min(r, e) - m
                info[i] = (
                    max(llen, rlen, lsuf + rpre),  # 合併區間長度
                    lpre + rpre * int(lpre == ln),  # 合併前綴
                    rsuf + lsuf * int(rsuf == rn),  # 合併後綴
                )
        return info[1]
    
    def query_sum(self, s, e):
        st = [(1, 1, self.n)]
        res = 0
        while st:
            i, l, r = st.pop()
            m = (l + r) // 2
            ln, rn = m - l + 1, r - m
            if s <= l and r <= e:
                res += self.tr[i]
                continue
            self.push(i, ln, rn)
            if s <= m: 
                st.append((i << 1, l, m))
            if m < e: 
                st.append((i << 1 | 1, m + 1, r))
        return res

def solve():
    tr = SegTree(a)
    for _ in range(m):
        k, l, r = MII()
        l += 1
        r += 1
        if k == 0:
            tr.modify(l, r, 'upd', 0)
        elif k == 1:
            tr.modify(l, r, 'upd', 1)
        elif k == 2:
            tr.modify(l, r, 'rev')
        elif k == 3:
            print(tr.query_sum(l, r))
        else:
            print(tr.query_len(l, r)[0])
            
               
for _ in range(1):
    n, m = MII()
    a = list(MII())
    solve()