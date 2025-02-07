from math import inf
from typing import List


class Solution:
    def numberOfSets(self, n: int, maxftance: int, roads: List[List[int]]) -> int:
        g = [[inf] * n for _ in range(n)]
        for i in range(n):
            g[i][i] = 0
        for x, y, w in roads:
            g[x][y] = g[y][x] = min(g[x][y], w)
        
        f = [None] * n
        def check(s: int) -> int:
            for i, gi in enumerate(g):
                if s >> i & 1:
                    f[i] = gi[:] # 淺複製
            
            for k in range(n):
                if (s >> k & 1) == 0: continue
                for i in range(n):
                    if (s >> i & 1) == 0 or f[i][k] == inf: continue
                    for j in range(i): # j<=i無向圖，取小於才有值
                        f[i][j] = f[j][i] = min(f[i][j], f[i][k] + f[k][j])
            
            for i, di in enumerate(f):
                if (s >> i & 1) == 0: continue
                if any(s >> j & 1 and d > maxftance for j, d in enumerate(di)):
                    return 0
            return 1
        return sum(check(s) for s in range(1 << n))