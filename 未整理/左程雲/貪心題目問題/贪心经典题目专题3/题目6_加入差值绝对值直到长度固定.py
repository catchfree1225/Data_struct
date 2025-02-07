import random as rand
from math import gcd
'''
题目6
加入差值绝对值直到长度固定
给定一个非负数组arr，计算任何两个数差值的绝对值
如果arr中没有，都要加入到arr里，但是只加一份
然后新的arr，继续计算任何两个数差值的绝对值
如果arr中没有，都要加入到arr里，但是只加一份
一直到arr大小固定，返回arr最终的长度
来自真实大厂笔试，没有在线测试，对数器验证
'''

def solve():
    a = sorted(set(arr))
    x = a[0]
    for y in a[1:]:
        x = gcd(x, y)
    return [i for i in range(x, a[-1] + 1, x)]
    
def naive():
    a = sorted(set(arr))
    while True:
        n = len(a)
        new_a = set()
        for i in range(n):
            for j in range(i + 1, n):
                d = abs(a[i] - a[j])
                if d and d not in a:
                    new_a.add(d)
        if not new_a:
            break
        a += list(new_a)
    return sorted(a)

print('測試開始')
for _ in range(20):
    arr = [rand.randint(1, 100) for _ in range(50)]
    cnt1, cnt2 = solve(), naive()
    if cnt1 != cnt2:
        print(f'出錯了 {cnt1}!={cnt2}')
    else:
        print(f'通過')
print('測試結束')
    