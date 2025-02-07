from math import inf

def getSum(arr):
    ans, s = -inf, 0
    for x in arr:
        s += x
        ans = max(ans, s)
        if s < 0:
            s = 0
    return ans
            
def naive():
    ans = getSum(a)
    for i in range(n):
        for j in range(i + 1, n):
            b = a[:i] + a[i:j][::-1] + a[j:]
            ans = max(ans, getSum(b))
    return ans
        
def solve():
    suf = [0]
    mx, s = -inf, 0
    for x in reversed(a):
        s += x
        mx = max(mx, s)
        suf.append(mx)
        if s < 0:
            s = 0
    suf.reverse()
    
    ans = -inf
    s = 0
    for i, x in enumerate(a):
        s += x
        ans = max(ans, s + max(suf[i + 1], 0))
        if s < 0:
            s = 0
    return ans
    

import random
print('測試開始')
for t in range(1, 10):
    n = random.randint(100, 1000)
    # 隨機生成數組元素，使用不同範圍和分佈
    if t % 2:
        a = [random.randint(-1000, 2000) for _ in range(n)]
    else: # 隨機正負數
        a = [random.choice([-1, 1]) * random.randint(0, 2000) for _ in range(n)]  
    cnt1, cnt2 = naive(), solve()
    if cnt1 != cnt2:
        print(f'{t}: 出錯了 {cnt1}!={cnt2}')
print('測試結束')
    