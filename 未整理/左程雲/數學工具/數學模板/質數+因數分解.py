from collections import Counter
from math import isqrt

N = int(1e5)
divs = [[] for _ in range(N + 1)]
is_prime = [False, True] * (N // 2 + 1)
is_prime[1], is_prime[2] = False, True
del is_prime[n+1:]
for i in range(3, isqrt(N) + 1, 2):
    if is_prime[i]:
        is_prime[i*i::i*2] = [False] * ((N - i * i) // (i * 2) + 1)
        
#質因子尋找
for j in range(2, N + 1, 2):
    divs[j].append(2)
for i in range(3, N + 1, 2):
    if is_prime[i]:
        for j in range(i, N + 1, i):
            divs[j].append(i)

# 因子尋找
for i in range(1, N + 1):
    for j in range(i, N + 1, i):
        divs[j].append(i)
        
# 質因子分解
def factorize(x):
    ct = Counter()
    for i in range(2, isqrt(x) + 1):
        while x and x % i == 0:
            x //= i
            ct[i] += 1
    if x > 1:
        ct[x] = 1
    return ct

# 找真因子
def getDivs(n):
    divs = []
    for i in range(1, isqrt(n) + 1):
        if n % i == 0:
            divs.append(i)
            if i != n // i:
                divs.append(n // i)
    return divs


class Solution:
    # 調和級數枚舉，不會重複枚舉: n + m + (u/k)*lgm
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        ct1 = Counter(x // k for x in nums1 if x % k == 0)
        if not ct1:
            return 0
        ct2 = Counter(nums2)
        ans = 0
        u = max(ct1)
        for i, c in ct2.items():
            s = sum(ct1[j] for j in range(i, u + 1, i))
            ans += s * c
        return ans
        
    # n*sqrt(u/k) + m
    def numberOfPairs2(self, nums1: List[int], nums2: List[int], k: int) -> int:
        def divisors(n):
            divs = []
            for i in range(1, isqrt(n) + 1):
                if n % i == 0:
                    divs.append(i)
                    if i != n // i:
                        divs.append(n // i)
            return divs
        
        divs_a = Counter()
        for x in nums1:
            divs_a.update(divisors(x))
        return sum(divs_a[x * k] for x in nums2)
