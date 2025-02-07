from math import isqrt
import sys
input = lambda: sys.stdin.readline().strip()
MII = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())

class SegTree:
    def __init__(self, init):
        self.n = len(init)
        self.tr_sum = [0] * self.n + init
        self.tr_max = [0] * self.n + init
        for i in range(self.n - 1, 0, -1):
            self.tr_sum[i] = self.tr_sum[i << 1] + self.tr_sum[i << 1 | 1]
            self.tr_max[i] = max(self.tr_max[i << 1], self.tr_max[i << 1 | 1])
    
    def apply(self, i):
        st = [(0, i)]
        while st:
            stat, i = st.pop()
            if stat == 0:
                if self.tr_max[i] <= 1:
                    continue
                if i >= n:
                    self.tr_sum[i] = isqrt(self.tr_sum[i])
                    self.tr_max[i] = isqrt(self.tr_max[i])
                else:
                    st.append((1, i))
                    st.append((0, i << 1))
                    st.append((0, i << 1 | 1))
            else:
                self.tr_sum[i] = self.tr_sum[i << 1] + self.tr_sum[i << 1 | 1]
                self.tr_max[i] = max(self.tr_max[i << 1], self.tr_max[i << 1 | 1])
    
    def pull(self, i):
        while i > 1:
            i >>= 1  
            self.tr_sum[i] = self.tr_sum[i << 1] + self.tr_sum[i << 1 | 1]
            self.tr_max[i] = max(self.tr_max[i << 1], self.tr_max[i << 1 | 1])
    
    def update(self, l, r):
        l += self.n
        r += self.n
        l0, r0 = l, r
        while l <= r:
            if l & 1:
                self.apply(l) 
                l += 1
            if not r & 1:
                self.apply(r)
                r -= 1
            l >>= 1
            r >>= 1
        self.pull(l0), self.pull(r0)
    
    def modify(self, i, val):
        i += n
        self.tr_sum[i] = self.tr_max[i] = val
        while i > 1:
            i >>= 1
            self.tr_sum[i] = self.tr_sum[i << 1] + self.tr_sum[i << 1 | 1]
            self.tr_max[i] = max(self.tr_max[i << 1], self.tr_max[i << 1 | 1])
    
    def query(self, l, r): #[l, r]
        l += self.n
        r += self.n
        res_sum = res_max = 0
        while l <= r:
            if l & 1: # 左子樹
                res_sum += self.tr_sum[l]
                res_max = max(res_max, self.tr_max[l])
                l += 1
            if not r & 1: # 右子樹
                res_sum += self.tr_sum[r]
                res_max = max(res_max, self.tr_max[r])
                r -= 1
            l >>= 1
            r >>= 1
        return res_sum, res_max

def solve():
    tr = SegTree(a)
    for _ in range(m):
        k, l, r = GMI()
        if l > r:
            l, r = r, l
        if k == -1:
            tr.update(l, r)
        else:
            print(tr.query(l, r)[0])        
               
for _ in range(1):
    n = int(input())
    a = list(MII())
    m = int(input())
    solve()