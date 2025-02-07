class PreSum2D:
    def __init__(self, arr):
        self.m, self.n = len(arr), len(arr[0])
        self.a = [[0] * (self.n + 2) for _ in range(self.m + 2)]
        for i, row in enumerate(arr):
            for j, x in enumerate(row):
                self.add(i, j, i, j, x)
        self.flg = False
        
    def accum(self):
        self.flg = True
        for i in range(self.m):
            for j in range(self.n):
                self.a[i + 1][j + 1] += self.a[i][j + 1] + self.a[i + 1][j] - self.a[i][j]        
                
    def add(self, i1, j1, i2, j2, x):
        self.a[i2 + 2][j2 + 2] += x
        self.a[i2 + 2][j1 + 1] -= x
        self.a[i1 + 1][j2 + 2] -= x
        self.a[i1 + 1][j1 + 1] += x
        
    def query(self, i1, j1, i2, j2):
        if not self.flg: self.accum(), self.accum()
        return self.a[i2 + 1][j2 + 1] - self.a[i2 + 1][j1] - self.a[i1][j2 + 1] + self.a[i1][j1]