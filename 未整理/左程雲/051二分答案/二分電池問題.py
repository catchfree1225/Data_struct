from bisect import bisect_right
from itertools import accumulate
from typing import List

class Solution:
    def maxRunTime_(self, n: int, batteries: List[int]) -> int:
        m = len(batteries)
        batteries.sort()
        ps = list(accumulate(batteries, initial=0))
        def check(t: int) -> bool:
            i = bisect_right(batteries, t) # 超過t的下標
            need = n - (m - i) # m-i: 已滿足的數量
            frag_batteries = ps[i] # <= t 的碎片電池電量
            return frag_batteries >= t * need
        
        l, r = -1, ps[-1] // n + 1
        while l + 1 < r:
            mid = l + (r - l) // 2
            if check(mid):
                l = mid
            else:
                r = mid
        return l

    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        batteries.sort(reverse=True)
        s = sum(batteries)
        for x in batteries:
            if x <= s // n: return s // n
            s -= x
            n -= 1
        return -1
