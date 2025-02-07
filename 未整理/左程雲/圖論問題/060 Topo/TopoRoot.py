class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        g = [[] for _ in range(n)]
        ind = [0] * n
        for x, y in richer: # 從最有錢的開始遍歷(root)
            g[x].append(y)
            ind[y] += 1

        q = deque([i for i, x in enumerate(ind) if x == 0])
        ans = list(range(n))
        while q:
            x = q.popleft()
            for y in g[x]:
                if quiet[ans[x]] < quiet[ans[y]]: # 可以用根更新後面
                    ans[y] = ans[x]
                ind[y] -= 1
                if ind[y] == 0:
                    q.append(y)
        return ans
