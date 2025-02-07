from collections import Counter, defaultdict
from math import inf
from typing import List

class Solution:
    def maxSumBST_(self, root) -> int:
        ans = 0 # 都不選
        def dfs(x) -> int:
            if x is None:
                return inf, -inf, 0
            l_min, l_max, l_sz = dfs(x.left)
            r_min, r_max, r_sz = dfs(x.right)
            nonlocal ans
            if l_max < x.val < r_min:
                ans = max(ans, x.val + l_sz + r_sz)
                return min(l_min, x.val), max(r_max, x.val), x.val + l_sz + r_sz
            else:
                return -inf, inf, max(l_sz, r_sz) # 不會是答案
        dfs(root)
        return ans

    def maxSumBST(self, root) -> int:     
        ans = 0
        vis, info = set(), defaultdict(lambda: (inf, -inf, 0))
        st = [root]
        while st:
            x = st[-1]
            if x is None:
                st.pop()
            elif x in vis:
                st.pop()
                l_min, l_max, l_sz = info[x.left]
                r_min, r_max, r_sz = info[x.right]
                if l_max < x.val < r_min:
                    ans = max(ans, x.val + l_sz + r_sz)
                    info[x] = min(l_min, x.val), max(r_max, x.val), x.val + l_sz + r_sz
                else:
                    info[x] = -inf, inf, -inf # 非BST
            else:
                vis.add(x)
                st += [x.left, x.right]
        return ans

class Solution:
    def largestBSTSubtree_(self, root) -> int:
        def dfs(x) -> int:
            if x is None:
                return inf, -inf, 0
            l_min, l_max, l_sz = dfs(x.left)
            r_min, r_max, r_sz = dfs(x.right)
            if l_max < x.val < r_min:
                return min(l_min, x.val), max(r_max, x.val), 1 + l_sz + r_sz
            else:
                return -inf, inf, max(l_sz, r_sz)
        return dfs(root)[2]

    def largestBSTSubtree(self, root) -> int:
        vis, info = set(), defaultdict(lambda: (inf, -inf, 0))
        st = [root]
        while st:
            x = st[-1]
            if x is None:
                st.pop()
            elif x in vis: # 如果節點已經訪問過，則計算結果
                st.pop()
                l_min, l_max, l_sz = info[x.left]
                r_min, r_max, r_sz = info[x.right]

                if l_max < x.val < r_min:
                    info[x] = min(l_min, x.val), max(r_max, x.val), 1 + l_sz + r_sz
                else:
                    info[x] = -inf, inf, max(l_sz, r_sz)
            else:
                vis.add(x)
                st += [x.left, x.right]
        return info[root][2]

class Solution:
    def diameterOfBinaryTree_(self, root) -> int:
        ans = 0
        def dfs(x): # 返回深度(邊數)
            if x is None:
                return -1
            dep_l, dep_r = dfs(x.left), dfs(x.right)
            nonlocal ans
            ans = max(ans, 2 + dep_l + dep_r)
            return 1 + max(dep_l, dep_r)
        dfs(root)
        return ans

    def diameterOfBinaryTree(self, root) -> int:
        ans = 0
        vis, info = set(), defaultdict(lambda: -1)
        st = [root]
        while st:
            x = st[-1]
            if x is None:
                st.pop()
            elif x in vis:
                st.pop()
                dep_l, dep_r = info[x.left], info[x.right]
                ans = max(ans, 2 + dep_l + dep_r)
                info[x] = 1 + max(dep_l, dep_r)
            else:
                vis.add(x)
                st += [x.left, x.right]
        return ans

class Solution:
    def distributeCoins(self, root) -> int:
        ans = 0
        def dfs_naive(x):
            if x is None:
                return 0, 0
            coins_l, nodes_l = dfs(x.left)
            coins_r, nodes_r = dfs(x.right)
            coins = x.val + coins_l + coins_r
            nodes = 1 + nodes_l + nodes_r
            nonlocal ans
            ans += abs(coins - nodes)
            return coins, nodes

        def dfs(x):
            if x is None:
                return 0
            diff_l, diff_r = dfs(x.left), dfs(x.right)
            diff = (x.val - 1) + diff_l + diff_r
            nonlocal ans
            ans += abs(diff)
            return diff
        dfs(root)
        return ans

class Solution:
    def pathSum(self, root, targetSum: int) -> int:
        ct = Counter([0])
        def dfs(x, s: int):
            if x is None:
                return 0
            # dfs前
            s += x.val
            res = ct[s - targetSum]
            ct[s] += 1
            # dfs後
            res += dfs(x.left, s) + dfs(x.right, s)
            ct[s] -= 1
            return res

        vis, info = set(), Counter()
        st = [(root, 0)]
        while st:
            x, s = st[-1] # 等於dfs入參
            if x is None:
                st.pop()
                continue
            s += x.val
            if x not in vis: # dfs前
                vis.add(x)      
                ct[s] += 1
                st += [(x.left, s), (x.right, s)]
            else: # dfs後
                st.pop()
                ct[s] -= 1
                info[x] = ct[s - targetSum] + info[x.left] + info[x.right]
        return info[root]

class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        n = len(roads) + 1
        g = [[] for _ in range(n)]
        for x, y in roads:
            g[x].append(y)
            g[y].append(x)
        
        ans = 0 # 貢獻法，計算從x往上邊，對整體ans的貢獻
        def dfs(x: int, fa: int):
            sz = 1
            for y in g[x]:
                if y == fa: continue
                sz += dfs(y, x)
            nonlocal ans # 計算貢獻，當作都匯聚到x
            ans += (sz + seats - 1) // seats * int(x != 0) # root不算
            return sz
        # dfs(0, -1)

        vis, info = [False] * n, [0] * n
        st = [(0, -1)]
        while st:
            x, fa = st[-1]
            if not vis[x]:
                vis[x] = True
                st += [(y, x) for y in g[x] if y != fa]
            else:
                st.pop()
                info[x] = 1 + sum(info[y] for y in g[x] if y != fa)
                ans += (info[x] + seats - 1) // seats * int(x != 0)
        return ans
