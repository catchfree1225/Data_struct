import sys
input = lambda: sys.stdin.readline().strip()
MII = lambda: map(int, input().split())

def solve():
    cap, must_buy_gain = X, 0
    games = []
    for _ in range(n):
        a, b, happy = MII()
        price = b - (a - b)
        if price < 0:
            cap += -price
            must_buy_gain += happy
        else:
            games.append((price, happy))
    games.sort()

    f = [0] * (cap + 1)
    hi = 0
    for price, happy in games:
        hi += price
        for i in range(min(hi, cap), price - 1, -1):
            f[i] = max(f[i], f[i - price] + happy)
    print(max(f) + must_buy_gain)
               
for _ in range(1):
    n, X = MII()
    solve()


# 求方法數
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # S_pos - S_neg = target
        # S_pos + S_neg = tot
        # => S_pos * 2 = target + tot 
        tot = sum(nums)
        cap = target + tot
        if cap % 2 or tot < abs(target):
            return 0

        nums.sort()
        cap //= 2
        f = [1] + [0] * cap
        hi = 0
        for x in nums:
            hi += x
            for i in range(min(hi, cap), x - 1, -1):
                f[i] += f[i - x]
        return f[cap]
