from collections import deque
from heapq import heappop, heappush
from math import inf
from typing import List

class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        m, n = len(grid), len(grid[0])
        k = sum(c.islower() for row in grid for c in row)
        si, sj = next((i, j) for i in range(m) for j in range(n) if grid[i][j] == '@')
        vis = {(0, si, sj)}
        q = deque([(0, si, sj)])
        t = 0
        while q:
            for _ in range(len(q)):
                s, x, y = q.popleft()
                if s == (1 << k) - 1:
                    return t
                for nx, ny in (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1):
                    if not (0 <= nx < m and 0 <= ny < n): continue
                    c, ns = grid[nx][ny], s
                    if c == '#' or c.isupper() and s >> (ord(c) - ord('A')) & 1 == 0: continue
                    if c.islower():
                        ns |= 1 << (ord(c) - ord('a'))
                    if (ns, nx, ny) not in vis:
                        vis.add((ns, nx, ny))
                        q.append((ns, nx, ny))
            t += 1
        return -1

class Solution:
    def electricCarPlan(self, paths: List[List[int]], cnt: int, start: int, end: int, charge: List[int]) -> int:
        n = len(charge)
        g = [[] for _ in range(n)]
        for x, y, w in paths:
            g[x].append((y, w))
            g[y].append((x, w))

        dis = [[inf] * (cnt + 1) for _ in range(n)]
        dis[start][0] = 0
        q = [(0, start, 0)]
        while q:
            tx, x, bx = heappop(q)
            if tx > dis[x][bx]:
                continue
            if x == end:
                return tx
            # 法1:不充電，但要夠能量走
            for y, wt in g[x]:
                if bx >= wt and dis[y][bx - wt] > tx + wt:
                    dis[y][bx - wt] = tx + wt
                    heappush(q, (tx + wt, y, bx - wt))
            # 法2:擴點充電，走1就好(後面會自動擴到cnt)
            if bx < cnt and dis[x][bx + 1] > tx + charge[x]:
                dis[x][bx + 1] = tx + charge[x]
                heappush(q, (tx + charge[x], x, bx + 1))
        return -1
