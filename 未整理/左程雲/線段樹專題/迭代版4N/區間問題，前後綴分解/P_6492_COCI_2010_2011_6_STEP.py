import sys
input = lambda: sys.stdin.readline().strip()
MII = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())

class SegTree: # 單點修改沒有push, apply, d數組
    def __init__(self, init):
        self.n = init
        m = 2 << self.n.bit_length()
        self.arr = [0] * (init + 1)
        self.len, self.pre, self.suf = [0] * m, [0] * m, [0] * m
        self.build()
        
    def pull(self, i, ln, rn, m):
        l, r = i << 1, i << 1 | 1
        self.len[i] = max(self.len[l], self.len[r])
        self.pre[i] = self.pre[l]
        self.suf[i] = self.suf[r]
        if self.arr[m] != self.arr[m + 1]:
            self.len[i] = max(self.len[i], self.suf[l] + self.pre[r])
            self.pre[i] += self.pre[r] * int(self.pre[l] == ln)
            self.suf[i] += self.suf[l] * int(self.suf[r] == rn)
 
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
                self.pull(i, ln, rn, m)

    def modify(self, u):
        st = [(0, 1, 1, self.n)]
        while st:
            stat, i, l, r = st.pop()
            m = (l + r) // 2
            ln, rn = m - l + 1, r - m
            if stat == 0:
                if l == r: # 單點修改
                    self.arr[u] ^= 1
                    continue
                st.append((1, i, l, r))
                if u <= m: 
                    st.append((0, i << 1, l, m))
                if m < u: 
                    st.append((0, i << 1 | 1, m + 1, r))
            else:
                self.pull(i, ln, rn, m)

def solve():
    tr = SegTree(n)
    for _ in range(m):
        i = int(input())
        tr.modify(i)
        print(tr.len[1])
               
for _ in range(1):
    n, m = MII()
    solve()