import sys
input = lambda: sys.stdin.readline().strip()
MII = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())

class SegTree:
    def __init__(self, init):
        self.n = init
        self.tr_s = [0] * (self.n << 1)
        self.tr_e = [0] * (self.n << 1)
    
    def addStart(self, i, val):
        i += self.n        
        self.tr_s[i] += val 
        while i > 1:
            i >>= 1
            self.tr_s[i] = self.tr_s[i << 1] + self.tr_s[i << 1 | 1]
    
    def addEnd(self, i, val):
        i += n        
        self.tr_e[i] += val
        while i > 1:
            i >>= 1
            self.tr_e[i] = self.tr_e[i << 1] + self.tr_e[i << 1 | 1]
    
    def query(self, l, r): #[l, r]
        l += self.n
        r += self.n
        res_s = res_e = 0
        while l <= r:
            if l & 1: # 左子樹
                res_s += self.tr_s[l]
                res_e += self.tr_e[l]
                l += 1
            if not r & 1: # 右子樹
                res_s += self.tr_s[r]
                res_e += self.tr_e[r]
                r -= 1
            l >>= 1
            r >>= 1
        return res_s, res_e

def solve():
    tr = SegTree(n)
    for _ in range(m):
        q, l, r = GMI()
        if q == 0:
            tr.addStart(l, 1)
            tr.addEnd(r, 1)
        else:
            ends = tr.query(0, l - 1)[1]
            starts = tr.query(0, r)[0]
            print(starts - ends)
               
for _ in range(1):
    n, m = MII()
    solve()