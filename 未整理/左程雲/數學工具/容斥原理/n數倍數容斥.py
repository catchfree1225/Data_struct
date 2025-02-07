from math import lcm
from typing import List

class Solution: # 「不能」组合使用不同面额的硬币，等於算該數的倍數有幾個
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        coins = sorted(set(coins)) # 去重+互質優化
        coprimes = []
        for x in coins:
            if all(x % y for y in coprimes):
                coprimes.append(x)
        coins = coprimes

        n = len(coins)
        def check(num: int) -> bool:
            cnt = 0
            for stat in range(1, 1 << n):
                x = 1
                sign = -1
                for i in range(n):
                    if stat >> i & 1:
                        sign *= -1
                        x = lcm(x, coins[i])
                cnt += num // x * sign
            return cnt >= k

        l, r = 0, coins[0] * k + 1 # 隨便乘k都會滿足需求
        while l + 1 < r:
            mid = l + (r - l) // 2
            if check(mid):
                r = mid
            else:
                l = mid
        return r
