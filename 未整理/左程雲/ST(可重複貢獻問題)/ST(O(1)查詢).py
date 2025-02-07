from collections import defaultdict
class SparseTable: # O(1)查询区间最值/sum/gcd/lcm
    def __init__(self, init, func=sum):
        self.st = [init]
        self.func = func
        j, n = 1, len(init)
        while j * 2 <= n + 1:
            pre = self.st[-1]
            self.st.append([func(pre[i], pre[i + j]) for i in range(n - j * 2 + 1)])
            j <<= 1

    def query(self, l, r): # [l, r] 
        k = (r - l + 1).bit_length() - 1
        return self.func(self.st[k][l], self.st[k][r - (1 << k) + 1])

class Solution: # 3113. 边界元素是最大值的子数组数目
    def numberOfSubarrays(self, nums: list[int]) -> int: # 1500ms
        st = SparseTable(nums, max)
        m = defaultdict(list)
        for i, x in enumerate(nums):
            m[x].append(i)
        
        ans = len(nums)
        for x, ids in m.items():
            n = len(ids)
            i = 0
            while i < n:
                j = i + 1
                while j < n and st.query(ids[i], ids[j]) == x:
                    j += 1
                cnt = j - i
                ans += cnt * (cnt - 1) // 2
                i = j
        return ans 
    
    def numberOfSubarrays_(self, nums: list[int]) -> int: # 165ms
        ans = len(nums)
        st = [[int(1e18), 0]] # 無窮大哨兵
        for x in nums:
            while x > st[-1][0]:
                st.pop()
            if x == st[-1][0]:
                ans += st[-1][1]
                st[-1][1] += 1
            else:
                st.append([x, 1])
        return ans