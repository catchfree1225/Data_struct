from math import inf
from collections import deque
            
def naive():
    ans = -inf
    for i in range(n - k):
        b = a[i:i+k+1]
        ans = max(ans, sum(b) - min(b))
    return ans
        
def solve():
    ans, s = -inf, 0
    q = deque()
    # 長度為k+1, i - j <= k
    # 此題要先插入後計算答案
    for i, x in enumerate(a):
        # 單調遞增，找最小值
        while q and a[q[-1]] >= x:
            q.pop()
        # 處理隊列長度
        q.append(i)
        if i - q[0] >= k + 1:
            q.popleft()
        # 隊頭為窗口最小值
        s += x
        if i >= k:
            if i > k: s -= a[i - (k + 1)]
            ans = max(ans, s - a[q[0]])
    return ans
    

import random
print('測試開始')
for t in range(1, 20):
    n = random.randint(10, 200)
    k = random.randint(1, n)
    # 隨機生成數組元素，使用不同範圍和分佈
    if t % 2:
        a = [random.randint(-1000, 2000) for _ in range(n)]
    else: # 隨機正負數
        a = [random.choice([-1, 1]) * random.randint(0, 2000) for _ in range(n)]  
    cnt1, cnt2 = naive(), solve()
    if cnt1 != cnt2:
        print(f'{t}: 出錯了 {cnt1}!={cnt2}')
print('測試結束')
    