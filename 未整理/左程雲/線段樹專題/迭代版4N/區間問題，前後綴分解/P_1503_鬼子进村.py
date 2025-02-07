import sys
input = lambda: sys.stdin.readline().strip()
MII = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())

class SegTree: # 單點修改沒有push, apply, d數組
    def __init__(self, init):
        self.n = init
        m = 2 << self.n.bit_length()
        self.pre, self.suf = [0] * m, [0] * m
        self.build()
        
    def pull(self, i, ln, rn):
        l, r = i << 1, i << 1 | 1
        self.pre[i] = self.pre[l] + self.pre[r] * int(self.pre[l] == ln)
        self.suf[i] = self.suf[r] + self.suf[l] * int(self.suf[r] == rn)
 
    def build(self):
        st = [(0, 1, 1, self.n)]
        while st:
            stat, i, l, r = st.pop()
            m = (l + r) // 2
            ln, rn = m - l + 1, r - m
            if stat == 0:
                if l == r:
                    self.pre[i] = self.suf[i] = 1
                    continue
                st.append((1, i, l, r))
                st.append((0, i << 1, l, m))
                st.append((0, i << 1 | 1, m + 1, r))
            else:
                self.pull(i, ln, rn)

    def modify(self, u, val):
        st = [(0, 1, 1, self.n)]
        while st:
            stat, i, l, r = st.pop()
            m = (l + r) // 2
            ln, rn = m - l + 1, r - m
            if stat == 0:
                if l == r: # 單點修改
                    self.pre[i] = self.suf[i] = val
                    continue
                st.append((1, i, l, r))
                if u <= m: 
                    st.append((0, i << 1, l, m))
                if m < u: 
                    st.append((0, i << 1 | 1, m + 1, r))
            else:
                self.pull(i, ln, rn)
    
    def query(self, u):
        st = [(1, 1, self.n)]
        while st: # 無修改數組，不用特別紀錄順序，可直接return
            i, l, r = st.pop()
            if l == r:
                return self.pre[i]
            m = (l + r) // 2
            ls, rs = i << 1, i << 1 | 1
            if u <= m: 
                if m - u + 1 <= self.suf[ls]:
                    return self.suf[ls] + self.pre[rs]
                else:
                    st.append((ls, l, m))
            if m < u: 
                if u - m <= self.pre[rs]:
                    return self.pre[rs] + self.suf[ls]
                else:
                    st.append((rs, m + 1, r))
    
def solve():
    tr = SegTree(n)
    destroy = []
    for _ in range(m):
        q = tuple(input().split())
        if q[0] == 'D':
            destroy.append(int(q[1]))
            tr.modify(destroy[-1], 0)
        elif q[0] == 'R':
            tr.modify(destroy.pop(), 1)
        else:
            print(tr.query(int(q[1])))
               
for _ in range(1):
    n, m = MII()
    solve()