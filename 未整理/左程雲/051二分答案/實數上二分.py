from typing import List

class Solution:
    def kthSmallestPrimeFraction(self, a: List[int], k: int) -> List[int]:
        n = len(a)
        # q = [(a[0] / a[-1], 0, n - 1)]
        # for _ in range(k - 1):
        #     _, i, j = heappop(q)
        #     if i + 1 < j:
        #         heappush(q, (a[i + 1] / a[j], i + 1, j))
        #         if i == 0:
        #             heappush(q, (a[i] / a[j - 1], i, j - 1))
        # return [a[q[0][1]], a[q[0][2]]]

        eps = 1e-8
        ai = aj = -1
        def check(num: int) -> bool:
            cnt = i = 0
            for j in range(1, n):
                while a[i + 1] / a[j] <= num: 
                    i += 1
                if a[i] / a[j] <= num:
                    cnt += i + 1
                if abs(a[i] / a[j] - num) < eps:
                    nonlocal ai, aj
                    ai, aj = a[i], a[j]
            return cnt >= k
        
        l, r = -eps, 1 + eps
        while l + eps < r: # 實數間隔為eps
            mid = (l + r) / 2
            if check(mid):
                r = mid
            else:
                l = mid
        return [ai, aj]
