class BIT:
    def __init__(self, n, arr=[]):
        self.tr = [0] * (n + 1)
        for i, x in enumerate(arr, 1):
            self.tr[i] += x
            if (ni := i + (i & -i)) < len(self.tr):
                self.tr[ni] += self.tr[i]
    
    def add(self, i, val):
        while i < len(self.tr):
            self.tr[i] += val
            i += i & -i
    
    def preSum(self, i):
        res = 0
        while i > 0:
            res += self.tr[i]
            i &= i - 1
        return res

class BIT2D:
    def __init__(self, m, n, arr=[]):
        self.m, self.n = m, n
        self.tr = [[[0] * 4 for _ in range(n + 1)] for _ in range(m + 1)]     
        for i, row in enumerate(arr):
            for j, x in enumerate(row):
                self.add(i, j, i, j, x)
                        
    def _add(self, row, col, val):
        i = row
        while i <= self.m:
            j = col
            while j <= self.n:
                t = self.tr[i][j]
                t[0] += val
                t[1] += val * row
                t[2] += val * col
                t[3] += val * row * col
                j += j & -j
            i += i & -i

    def add(self, i1, j1, i2, j2, x):
        self._add(i2 + 2, j2 + 2, x)
        self._add(i2 + 2, j1 + 1, -x)
        self._add(i1 + 1, j2 + 2, -x)
        self._add(i1 + 1, j1 + 1, x)
    
    def preSum(self, row, col):
        res, i = 0, row
        while i > 0:
            j = col
            while j > 0:
                t = self.tr[i][j]
                res += (row + 1) * (col + 1) * t[0]
                res -= (col + 1) * t[1]
                res -= (row + 1) * t[2]
                res += t[3]
                j &= j - 1
            i &= i - 1
        return res    
    
    def query(self, i1, j1, i2, j2):
        return self.preSum(i2 + 1, j2 + 1) - self.preSum(i1, j2 + 1) - \
               self.preSum(i2 + 1, j1) + self.preSum(i1, j1)