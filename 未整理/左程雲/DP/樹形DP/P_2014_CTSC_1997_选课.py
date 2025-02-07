from functools import cache
import sys
input = sys.stdin.readline

def solve():
    g = [[] for _ in range(n + 1)]
    nums = [0] * (n + 1)
    for i in range(1, n + 1):
        k, s = map(int, input().split())
        g[k].append(i)
        nums[i] = s
    
    # @cache
    # def dfs(x: int, i: int, k: int):
    #     if k == 1:
    #         return nums[x]
    #     res = 0
    #     for j in range(i, len(g[x])):
    #         y = g[x][j]
    #         for s in range(1, k):
    #             res = max(res, dfs(y, 0, s) + dfs(x, j + 1, k - s))
    #     return res
    # print(dfs(0, 0, m + 1)) # root多算一個
    
    dfn, in_, out = [], [0] * (n + 1), [0] * (n + 1)
    def dfs(x: int):
        dfn.append(x)
        in_[x] = len(dfn) - 1
        for y in g[x]:
            dfs(y)
        out[x] = len(dfn) - 1
    dfs(0)
    
    f = [[0] * (m + 2) for _ in range(n + 2)] # 多1避免+1超過
    for i in range(n, 0, -1): # dfn序號[1, n]
        for s in range(1, m + 1):
            x = dfn[i]
            f[i][s] = max(f[out[x] + 1][s], nums[x] + f[i + 1][s - 1])
    print(f[1][m])
            
for _ in range(1):
    n, m = map(int, input().split())
    solve()
    