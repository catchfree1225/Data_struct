class SegTree:
    def __init__(self, n, arr=[]):
        self.n = 1 << (n - 1).bit_length()
        self.sum = [0] * (self.n * 2)
        self.d = [0] * self.n
        if arr:
            self.sum[self.n:self.n+n] = arr
            for i in range(self.n - 1, 0, -1):
                self.sum[i] = self.sum[i << 1] + self.sum[i << 1 | 1]
    
    def mark(self, i, p, val):
        self.sum[i] += val << p
        if i < self.n: # 非葉子
            self.d[i] += val
    
    def pull(self, i):
        p = 0
        while i > 1:
            i >>= 1    
            p += 1
            self.sum[i] = self.sum[i << 1] + self.sum[i << 1 | 1] + (self.d[i] << p)
                
    def push(self, i):       
        for p in range(i.bit_length() - 1, 0, -1):
            if self.d[j := i >> p]:
                q, self.d[j] = self.d[j], 0
                self.mark(j << 1, p - 1, q)
                self.mark(j << 1 | 1, p - 1, q)
    
    def add(self, l, r, val):
        l = l0 = l + self.n
        r = r0 = r + self.n
        p = 0
        while l <= r:
            if l & 1:
                self.mark(l, p, val) 
                l += 1
            if not r & 1:
                self.mark(r, p, val)
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
                res_l += self.sum[l]
                l += 1
            if not r & 1: # 右子樹
                res_r += self.sum[r]
                r -= 1
            l >>= 1
            r >>= 1
        return res_l + res_r   