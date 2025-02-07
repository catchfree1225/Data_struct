class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        n = len(parent)
        g = [[] for _ in range(n)]
        for i in range(1, n):
            g[parent[i]].append(i)

        ans = 1 # 有可能不會被更新
        def dfs(x: int) -> int:
            nonlocal ans
            d1 = d2 = 0 
            for y in g[x]: 
                nd = dfs(y) # 一定要遞歸，子樹中可能有答案
                if s[x] != s[y]:
                    d2 = max(d2, nd)
                    if d2 > d1:
                        d1, d2 = d2, d1
                    ans = max(ans, 1 + d1 + d2)    
            return 1 + d1
        # dfs(0)

        vis, info = [False] * n, [0] * n
        st = [0]
        while st:
            x = st[-1]
            if not vis[x]:
                vis[x] = True
                st += g[x]
            else:
                st.pop()
                d1 = d2 = 0
                for y in g[x]:
                    nd = info[y]
                    if s[x] != s[y]:
                        d2 = max(d2, nd)
                        if d2 > d1:
                            d1, d2 = d2, d1
                        ans = max(ans, 1 + d1 + d2)
                info[x] = 1 + d1
        return ans
