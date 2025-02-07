from collections import deque
from typing import List

class Solution:
    def maximumInvitations(self, fav: List[int]) -> int:
        n = len(fav)
        def max_cycle():
            vis = [False] * n
            ans = 0
            for i in range(n):
                if vis[i]: continue
                cycle = []
                j = i
                while not vis[j]:
                    cycle.append(j)
                    vis[j] = True
                    j = fav[j]
                for k, v in enumerate(cycle):
                    if v == j:
                        ans = max(ans, len(cycle) - k) # k為環進入位置
                        break
            return ans

        def max_chain():
            ind = [0] * n
            for f in fav:
                ind[f] += 1
            deep = [0] * n # 從root來的最大深度
            q = deque([i for i, x in enumerate(ind) if x == 0])
            while q:
                x = q.popleft()
                y = fav[x]
                deep[y] = max(deep[y], deep[x] + 1)
                ind[y] -= 1
                if ind[y] == 0:
                    q.append(y)
            return sum(1 + deep[i] for i, fi in enumerate(fav) if i == fav[fi]) # 長度為2的環

        return max(max_cycle(), max_chain())

class Solution:
    def maximumInvitations(self, fav: List[int]) -> int:
        n = len(fav)
        ind = [0] * n
        for f in fav:
            ind[f] += 1

        deep = [0] * n # 從root來的最大深度
        q = deque([i for i, x in enumerate(ind) if x == 0])
        while q:
            x = q.popleft()
            y = fav[x]
            deep[y] = max(deep[y], deep[x] + 1)
            ind[y] -= 1
            if ind[y] == 0:
                q.append(y)

        maxRing = maxChain = 0
        for i, x in enumerate(ind): # 尋找環(ind!=0)
            if x == 0: continue
            ind[i] == 0
            ringSz = 1
            j = fav[i]
            while j != i: # 找環
                ind[j] = 0
                ringSz += 1
                j = fav[j]
            
            if ringSz == 2:
                maxChain += 2 + deep[i] + deep[fav[i]]
            else:
                maxRing = max(maxRing, ringSz)

        return max(maxRing, maxChain)
