from collections import Counter
from math import isqrt

N = int(1e5)
divs = [[] for _ in range(N + 1)]
is_prime = [False, True] * (N // 2 + 1)
is_prime[1], is_prime[2] = False, True
del is_prime[N+1:]
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

# 調和級數枚舉值域，離線詢問: n + m + (u/k)*lgm
from typing import List
# 3164. 优质数对的总数 II
def numberOfPairs(nums1: List[int], nums2: List[int], k: int) -> int:
    ct = Counter(x // k for x in nums1 if x % k == 0)
    ans, mx = 0, max(ct, default=0)
    for x, v in Counter(nums2).items():
        s = sum(ct[y] for y in range(x, mx + 1, x))
        ans += s * v
    return ans

# 3447. 将元素分配给有约束条件的组
def assignElements(groups: List[int], elements: List[int]) -> List[int]:
    mx = max(groups)
    qs = [-1] * (mx + 1) # 調和級數枚舉值域
    for i, x in enumerate(elements):
        if x > mx or qs[x] >= 0: # 太大或已標記過不會是因數
            continue
        for y in range(x, mx + 1, x):
            if qs[y] < 0:
                qs[y] = i
    return [qs[x] for x in groups] 