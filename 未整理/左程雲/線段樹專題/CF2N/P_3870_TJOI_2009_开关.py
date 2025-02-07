import sys
input = lambda: sys.stdin.readline().strip()
MII = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())

class SegTree:
    def __init__(self, init):
        self.n = init
        self.tr = [0] * (self.n << 1)
        self.rev = [False] * self.n
    
    def lazy(self, i, p):
        self.tr[i] = (1 << p) - self.tr[i]
        if i < self.n:
            self.rev[i] ^= True
    
    def pull(self, i):
        p = 0
        while i > 1:
            i >>= 1
            p += 1
            self.tr[i] = self.tr[i << 1] + self.tr[i << 1 | 1]
            if self.rev[i]:
                self.tr[i] = (1 << p) - self.tr[i]

    def push(self, i):      
        for p in range(i.bit_length() - 1, 0, -1):
            j = i >> p
            if self.rev[j]: 
                self.lazy(j << 1, p - 1)
                self.lazy(j << 1 | 1, p - 1)
                self.rev[j] = False
    
    def reverse(self, l, r):
        l += self.n
        r += self.n
        self.push(l), self.push(r)
        l0, r0 = l, r
        p = 0
        while l <= r:
            if l & 1:
                self.lazy(l, p) 
                l += 1
            if not r & 1:
                self.lazy(r, p)
                r -= 1
            l >>= 1
            r >>= 1
            p += 1
        self.pull(l0), self.pull(r0)
    
    def query(self, l, r): #[l, r]
        l += self.n
        r += self.n
        self.push(l), self.push(r)
        res = 0
        while l <= r:
            if l & 1: # 左子樹
                res += self.tr[l]
                l += 1
            if not r & 1: # 右子樹
                res += self.tr[r]
                r -= 1
            l >>= 1
            r >>= 1
        return res
    

def solve():
    tr = SegTree(n)
    for _ in range(m):
        c, a, b = GMI()
        if c == -1:
            tr.reverse(a, b)
        else:
            print(tr.query(a, b))
               
for _ in range(1):
    n, m = MII()
    solve()