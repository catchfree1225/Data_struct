class SparseTable:
    def __init__(self, arr, func, e):
        n, k = len(arr), len(arr).bit_length() - 1
        st = [arr] + [[e] * n for _ in range(k)]
        for p in range(k):
            for i in range(n - (1 << p)):
                st[p + 1][i] = func(st[p][i], st[p][i + (1 << p)])
        self.st, self.func = st, func
            
    def query(self, l, r):
        p = (r - l + 1).bit_length() - 1
        return self.func(self.st[p][l], self.st[p][r - (1 << p) + 1])
