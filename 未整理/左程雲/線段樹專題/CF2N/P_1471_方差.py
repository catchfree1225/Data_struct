import sys
input = lambda: sys.stdin.readline().strip()
MII = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())

class SegTree:
    def __init__(self, init):
        self.n = len(init)
        self.tr = [0] * self.n + init
        self.tr2 = [0] * self.n + [x ** 2 for x in init]
        for i in range(self.n - 1, 0, -1):
            self.tr[i] = self.tr[i << 1] + self.tr[i << 1 | 1]
            self.tr2[i] = self.tr2[i << 1] + self.tr2[i << 1 | 1]
        self.d = [0] * self.n
    
    def lazy(self, i, p, val):
        n = 1 << p
        self.tr2[i] += val ** 2 * n + 2 * self.tr[i] * val
        self.tr[i] += val * n
        if i < self.n: # 為parent
            self.d[i] += val
    
    def pull(self, i):
        n = 1
        while i > 1:
            i >>= 1
            n <<= 1 # 合併無關順序，更新才會看值
            self.tr[i] = self.tr[i << 1] + self.tr[i << 1 | 1]
            self.tr2[i] = self.tr2[i << 1] + self.tr2[i << 1 | 1]
            if val := self.d[i]:
                self.tr2[i] += val ** 2 * n + 2 * self.tr[i] * val
                self.tr[i] += val * n
                
    def push(self, i):        
        for p in range(i.bit_length() - 1, 0, -1):
            j = i >> p
            if self.d[j]: # 不可用elif, 有可能先修改後增加
                self.lazy(j << 1, p - 1, self.d[j])
                self.lazy(j << 1 | 1, p - 1, self.d[j])
                self.d[j] = 0     
    
    def modify(self, l, r, val):
        l += self.n
        r += self.n
        self.push(l), self.push(r)
        l0, r0 = l, r
        p = 0
        while l <= r:
            if l & 1:
                self.lazy(l, p, val) 
                l += 1
            if not r & 1:
                self.lazy(r, p, val)
                r -= 1
            l >>= 1
            r >>= 1
            p += 1
        self.pull(l0), self.pull(r0)
    
    def query(self, l, r): #[l, r]
        l += self.n
        r += self.n
        self.push(l), self.push(r)
        res_1 = res_2 = 0
        while l <= r:
            if l & 1: # 左子樹
                res_1 += self.tr[l]
                res_2 += self.tr2[l]
                l += 1
            if not r & 1: # 右子樹
                res_1 += self.tr[r]
                res_2 += self.tr2[r]
                r -= 1
            l >>= 1
            r >>= 1
        return res_1, res_2

def solve():
    tr = SegTree(a)
    for _ in range(m):
        q = tuple(input().split())  
        l, r = int(q[1]) - 1, int(q[2]) - 1
        if q[0] == '1': 
            k = float(q[3])
            tr.modify(l, r, k)
        elif q[0] == '2':
            s = tr.query(l, r)[0]
            print(f'{s / (r - l + 1):.4f}')
        else:
            s, s2 = tr.query(l, r)
            n = (r - l + 1)
            mu = s / n
            res = s2 / n - mu ** 2
            print(f'{res:.4f}')
               
for _ in range(1):
    n, m = MII()
    a = list(map(float, input().split()))
    solve()