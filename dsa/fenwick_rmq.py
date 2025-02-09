from math import inf
class BIT_rmq:
    def __init__(self, n, arr=[]):
        self.tr = [-inf] * (n + 1)
        self.a = [-inf] * (n + 1)
        for i, x in enumerate(arr, 1):
            self.set(i, x)
    
    def set(self, i, val):
        self.a[i] = val
        while i < len(self.tr):
            j, self.tr[i] = 1, self.a[i]
            while j < i & -i:
                self.tr[i] = max(self.tr[i], self.tr[i - j])
                j <<= 1
            i += i & -i
    
    def query(self, l, r):
        res = -inf
        while r >= l:
            res = max(self.a[r], res)
            r -= 1
            while r & (r - 1) >= l:
                res = max(res, self.tr[r])
                r &= r - 1
        return res

class SegTree:
    def __init__(self, n, arr=[]):
        self.n = 1 << (n - 1).bit_length()
        self.mx = [-inf] * (self.n * 2)
        if arr: 
            self.mx[self.n:self.n+n] = arr
            for i in range(self.n - 1, 0, -1):
                self.pull(i)
                
    def pull(self, i):
        self.mx[i] = max(self.mx[i << 1], self.mx[i << 1 | 1])
    
    def set(self, i, val):
        i += self.n        
        self.mx[i] = val
        while i > 1:
            i >>= 1
            self.pull(i)
    
    def query(self, l, r): #[l, r]
        l += self.n
        r += self.n
        res = -inf
        while l <= r:
            if l & 1: # 左子樹
                res = max(res, self.mx[l])
                l += 1
            if not r & 1: # 右子樹
                res = max(res, self.mx[r])
                r -= 1
            l >>= 1
            r >>= 1
        return res

import random, time
from math import log2

def test_rmq_structures(n=100, q=100, updates=50):
    # 生成測試數據
    arr = [random.randint(-1000, 1000) for _ in range(n)]
    
    # 初始化結構
    t1 = time.time()
    bit = BIT_rmq(n, arr)
    bit_init = time.time() - t1 + 1e-9
    
    t2 = time.time()
    seg = SegTree(n, arr)
    seg_init = time.time() - t2 + 1e-9
    
    # 測試查詢
    queries = [(random.randint(0, n-1), random.randint(0, n-1)) for _ in range(q)]
    queries = [(min(l,r), max(l,r)) for l,r in queries]
    
    # 正確性快速檢查（只檢查一次）
    l, r = queries[0]
    bit_res = bit.query(l+1, r+1)
    seg_res = seg.query(l, r)
    if bit_res != seg_res:
        print(f"Warning: Results differ! BIT={bit_res}, SEG={seg_res}")
    
    # 效能測試：查詢
    t1 = time.time()
    for l, r in queries:
        _ = bit.query(l+1, r+1)
    bit_time = time.time() - t1 + 1e-9
    
    t2 = time.time()
    for l, r in queries:
        _ = seg.query(l, r)
    seg_time = time.time() - t2 + 1e-9
    
    # 更新測試
    updates_list = [(random.randint(0, n-1), random.randint(-1000, 1000)) 
                    for _ in range(updates)]
    
    t1 = time.time()
    for i, val in updates_list:
        bit.set(i+1, val)
    bit_update = time.time() - t1 + 1e-9
    
    t2 = time.time()
    for i, val in updates_list:
        seg.set(i, val)
    seg_update = time.time() - t2 + 1e-9
    
    # 理論複雜度
    log_n = log2(n)
    
    print(f"Size: n={n}, Queries: q={q}, Updates: u={updates}")
    print(f"理論複雜度（log n = {log_n:.2f}）:")
    print(f"BIT: O(log n) = {log_n:.2f}")
    print(f"SEG: O(log n) = {log_n:.2f}")
    print("\n初始化時間:")
    print(f"BIT: {bit_init:.6f}s")
    print(f"SEG: {seg_init:.6f}s")
    print(f"比值: {bit_init/seg_init:.2f}x")
    print("\n查詢時間:")
    print(f"BIT: {bit_time:.6f}s ({q/bit_time:.0f} ops/s)")
    print(f"SEG: {seg_time:.6f}s ({q/seg_time:.0f} ops/s)")
    print(f"比值: {bit_time/seg_time:.2f}x")
    print("\n更新時間:")
    print(f"BIT: {bit_update:.6f}s ({updates/bit_update:.0f} ops/s)")
    print(f"SEG: {seg_update:.6f}s ({updates/seg_update:.0f} ops/s)")
    print(f"比值: {bit_update/seg_update:.2f}x")
    print("="*50)

# 測試不同規模
sizes = [
    (5000, 5000, 5000),
    (10000, 10000, 10000),
    (50000, 50000, 50000),
    (100000, 100000, 100000),
    (500000, 500000, 500000),
    (1000000, 10000000, 1000000)
]

for n, q, u in sizes:
    print(f"\nTest case n={n:,}, q={q:,}, u={u:,}")
    test_rmq_structures(n, q, u)