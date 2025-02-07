import sys
input = lambda: sys.stdin.readline().strip()
MII = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())

class SegTree:
    def __init__(self, init):
        if isinstance(init, int):
            self.n = init
            self.tr = [0] * (self.n << 1)
        else:
            self.n = len(init)
            self.tr = [0] * self.n + init
            for i in range(self.n - 1, 0, -1):
                self.tr[i] = self.tr[i << 1] + self.tr[i << 1 | 1]
        self.d = [0] * self.n
        self.upd = [None] * self.n
    
    def apply(self, i, p, val, isAdd):
        if isAdd:
            self.tr[i] += val << p
            if i < self.n: # 為parent
                self.d[i] += val
        else:
            self.tr[i] = val << p
            if i < self.n:
                self.d[i] = 0 # 覆蓋掉增加量
                self.upd[i] = val
    
    def pull(self, i):
        p = 0
        while i > 1:
            i >>= 1
            p += 1
            if self.upd[i] is not None:
                self.tr[i] = self.upd[i] << p   
            else:     
                self.tr[i] = self.tr[i << 1] + self.tr[i << 1 | 1] + (self.d[i] << p)
                
    def push(self, i):        
        for p in range(i.bit_length() - 1, 0, -1):
            j = i >> p
            if self.upd[j] is not None: # 先修改再增加
                self.apply(j << 1, p - 1, self.upd[j], False)
                self.apply(j << 1 | 1, p - 1, self.upd[j], False)
                self.upd[j] = None
            if self.d[j]: # 不可用elif, 有可能先修改後增加
                self.apply(j << 1, p - 1, self.d[j], True)
                self.apply(j << 1 | 1, p - 1, self.d[j], True)
                self.d[j] = 0     
    
    def modify(self, l, r, val, isAdd=True):
        l += self.n
        r += self.n
        self.push(l), self.push(r)
        l0, r0 = l, r
        p = 0
        while l <= r:
            if l & 1:
                self.apply(l, p, val, isAdd) 
                l += 1
            if not r & 1:
                self.apply(r, p, val, isAdd)
                r -= 1
            l >>= 1
            r >>= 1
            p += 1
        self.pull(l0), self.pull(r0)
    
    def query(self, l, r): #[l, r]
        l += self.n
        r += self.n
        self.push(l), self.push(r)
        res_l = res_r = 0
        while l <= r:
            if l & 1: # 左子樹
                res_l += self.tr[l]
                l += 1
            if not r & 1: # 右子樹
                res_r += self.tr[r]
                r -= 1
            l >>= 1
            r >>= 1
        return res_l + res_r

def solve():
    tr = SegTree(n + 10)
    def add_diffArr(l, r, k, d):
        e = k + (r - l) * d
        tr.modify(l, l, k)
        if l + 1 <= r:
            tr.modify(l + 1, r, d)
        tr.modify(r + 1, r + 1, -e)
    
    for _ in range(m):
        q = tuple(MII())
        if q[0] == 1:
            add_diffArr(q[1] - 1, q[2] - 1, q[3], q[4]) 
        else:
            print(tr.query(0, q[1] - 1) + a[q[1] - 1])
               
for _ in range(1):
    n, m = MII()
    a = list(MII())
    solve()