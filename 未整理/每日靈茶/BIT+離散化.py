#法一 BIT+離散化
from itertools import accumulate, chain
from typing import List

class BIT:
    def __init__(self, n):
        self.arr = [0] * (n + 1)
        self.n = n
    
    def lowbit(self, x):
        return x & -x
    
    def add(self, x, val):
        while x <= self.n:
            self.arr[x] += val
            x += self.lowbit(x)

    def sum(self, x):
        res = 0
        while x > 0:
            res += self.arr[x]
            x -= self.lowbit(x)
        return res

class Solution:
    def countRangeSum(self, nums: list[int], lower: int, upper: int) -> int:
        pre = accumulate(nums, initial=0)
        arr = []
        for s in pre:
            arr += [s, s - lower, s - upper]
        m = {x: i + 1 for i, x in enumerate(sorted(set(arr)))}

        tr = BIT(len(m))
        ans = 0
        for s in pre:
            l, r = m[s - upper], m[s - lower]
            ans += tr.sum(r) - tr.sum(l - 1)
            tr.add(m[s], 1)
        return ans

# 法二
from sortedcontainers import SortedList
class Solution:
    def countRangeSum(self, nums: list[int], lower: int, upper: int) -> int:
        sl = SortedList()
        ans = 0
        for s in accumulate(nums, initial=0):
            ans += sl.bisect_right(s - lower) - sl.bisect_left(s - upper)
            sl.add(s)
        return ans

class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        combined = list(chain.from_iterable(flowers)) + people
        m = {x: i for i, x in enumerate(sorted(set(combined)))}
        d = [0] * (len(m) + 1)
        for fr, to in flowers:
            d[m[fr]] += 1
            d[m[to] + 1] -= 1
        d = list(accumulate(d))
        return [d[m[p]] for p in people]

