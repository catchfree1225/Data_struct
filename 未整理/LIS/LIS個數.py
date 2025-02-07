class SegTree:
    def __init__(self, init):
        self.n = 1 << init.bit_length()
        self.tr = [[0] * 2 for _ in range(self.n << 1)]
    
    def calc(self, a, b):
        # tr[0]: len, tr[1]: cnt
        if a[0] == b[0]:
            return a[0], a[1] + b[1]
        else:
            return a if a[0] > b[0] else b
    
    def modify(self, i, val):
        i += self.n        
        self.tr[i] = self.calc(self.tr[i], val)
        while i > 1:
            i >>= 1
            self.tr[i] = self.calc(self.tr[i << 1], self.tr[i << 1 | 1])
    
    def query(self, l, r): #[l, r]
        l += self.n
        r += self.n
        res = 0, 0
        while l <= r:
            if l & 1: # 左子樹
                res = self.calc(res, self.tr[l])
                l += 1
            if not r & 1: # 右子樹
                res = self.calc(res, self.tr[r])
                r -= 1
            l >>= 1
            r >>= 1
        return res

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        m = {x: i for i, x in enumerate(sorted(set(nums)))}
        tr = SegTree(len(m))
        for x in nums:
            x = m[x]
            lng, cnt = tr.query(0, x - 1)
            tr.modify(x, (lng + 1, max(cnt, 1)))
        return tr.tr[1][1]
