import sys
input = sys.stdin.readline

class UnionFind:
    def __init__(self, n):
        self.p = list(range(n))
    
    def find(self, u): # 使用遞迴會超時
        rt = u
        while rt != self.p[rt]:
            rt = self.p[rt]
        while self.p[u] != rt:
            self.p[u], u = rt, self.p[u]
        return rt

    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu == pv: return False
        self.p[pv] = pu
        return True

def solve(): 
    uf = UnionFind(n + 1)
    water = [0] * n
    def add_water(i, val):
        while uf.find(i) < n and val:
            i = uf.find(i)
            max_add = min(cap[i] - water[i], val)
            val -= max_add
            water[i] += max_add
            if water[i] == cap[i]:
                uf.union(i + 1, i)
        
    for q in queries:
        i = q[1] - 1
        if q[0] == 1:
            add_water(i, q[2])
        else:
            print(water[i])
    
for _ in range(1):
    n = int(input())
    cap = list(map(int, input().split()))
    m = int(input())
    queries = [tuple(map(int, input().split())) for _ in range(m)]
    solve()
    