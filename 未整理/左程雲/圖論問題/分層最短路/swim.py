from collections import deque
from heapq import heappop, heappush
from math import inf
from typing import List

class Solution: #110ms
    def swimInWater(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        def check(t: int) -> bool:
            vis = [[False] * n for _ in range(m)]
            vis[0][0] = True
            q = deque([(0, 0)])
            while q:
                x, y = q.popleft()
                if x == m - 1 and y == n - 1:
                    return True
                for nx, ny in (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1):
                    if not (0 <= nx < m and 0 <= ny < n): continue
                    if not vis[nx][ny] and grid[nx][ny] <= t:
                        vis[nx][ny] = True
                        q.append((nx, ny))
            return False            

        l, r = grid[0][0] - 1, max(max(row) for row in grid) + 1
        while l + 1 < r:
            mid = (l + r) // 2
            if check(mid):
                r = mid
            else:
                l = mid
        return r

class Solution: #64ms
    def swimInWater(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dis = [[inf] * n for _ in range(m)]
        dis[0][0] = grid[0][0]
        q = [(grid[0][0], 0, 0)]
        while q:
            wf, x, y = heappop(q)
            if wf > dis[x][y]:
                continue
            for nx, ny in (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1):
                if not (0 <= nx < m and 0 <= ny < n): continue
                nw = max(wf, grid[nx][ny]) # 成本=此題dis
                if nw < dis[nx][ny]:
                    dis[nx][ny] = nw
                    heappush(q, (nw, nx, ny))
        return dis[-1][-1]

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

class Solution: # 70ms
    def swimInWater(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        li = [(i, j) for i in range(m) for j in range(n)]
        li.sort(key=lambda x: grid[x[0]][x[1]])
        uf = UnionFind(m * n)    
        for i, j in li:
            t = grid[i][j]
            for ni, nj in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] <= t:
                    uf.union(i * n + j, ni * n + nj)
            if uf.find(0) == uf.find(m * n - 1):
                return t
        return -1
