from cmath import inf
import sys
input = sys.stdin.readline

def solve():
    f = [[-inf] * n for _ in range(n)]
    f[0][0] = mat[0][0]
    for t in range(1, n * 2 - 1): # 走的步數
        for x1 in range(min(t, n - 1), max(t - n + 1, 0) - 1, -1):
            for x2 in range(min(t, n - 1), x1 - 1, -1):
                y1, y2 = t - x1, t - x2
                res = f[x1][x2] # 1,2都往下
                if x1:
                    res = max(res, f[x1 - 1][x2]) # 1往右
                if x2:
                    res = max(res, f[x1][x2 - 1]) # 2往右
                if x1 and x2:
                    res = max(res, f[x1 - 1][x2 - 1]) # 都往右
                res += mat[x1][y1] + mat[x2][y2] * int(x1 != x2)
                f[x1][x2] = res
    print(f[n - 1][n - 1])
    
    # def isValid(x, y):
    #     return 0 <= x < n and 0 <= y < n
    # @cache
    # def dfs(i: int, j: int, x: int, y: int) -> int:
    #     if i == n - 1 and j == n - 1:
    #         return mat[i][j]
    #     res = -inf
    #     for ni, nj in (i + 1, j), (i, j + 1):
    #         if not isValid(ni, nj): continue
    #         for nx, ny in (x + 1, y), (x, y + 1):
    #             if not isValid(nx, ny): continue
    #             res = max(res, dfs(ni, nj, nx, ny))
    #     return res + mat[x1][y1] + mat[x2][y2] * int((x1, y1) != (x2, y2))
    # ans = dfs(0, 0, 0, 0)
    # print(ans)        
               
for _ in range(1):
    n = int(input())
    mat = [tuple(map(int, input().split())) for _ in range(n)]
    solve()