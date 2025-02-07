'''
题目6
两个0和1数量相等区间的最大长度
给出一个长度为n的01串，现在请你找到两个区间
使得这两个区间中，1的个数相等，0的个数也相等
这两个区间可以相交，但是不可以完全重叠，即两个区间的左右端点不可以完全一样
现在请你找到两个最长的区间，满足以上要求
返回区间最大长度
来自真实大厂笔试，没有在线测试，对数器验证
'''
def solve():
    left0 = left1 = n
    right0 = right1 = -1
    for i, x in enumerate(a):
        if x == 0:
            left0 = min(left0, i)
            right0 = max(right0, i)
        else:
            left1 = min(left1, i)
            right1 = max(right1, i)
    return max(right0 - left0, right1 - left1)
     
def naive():
    for L in range(n - 1, 0, -1):
        for i in range(n - L + 1):
            for j in range(i + 1, n - L + 1):
                if sorted(a[i:i+L]) == sorted(a[j:j+L]):
                    return L
    
import random
rnd = random.randint
print('測試開始')
for _ in range(50):
    n = rnd(2, 2000)
    a = [rnd(0, 1) for _ in range(n)]
    res_naive, res_solve = naive(), solve()
    if res_naive != res_solve:
        print(f'出錯了!! {res_naive} != {res_solve}')
        print(a)
    print('-------------------------')
print('測試結束')