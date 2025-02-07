'''
题目4
平均值最小累加和
给定一个数组arr，长度为n
再给定一个数字k，表示一定要将arr划分成k个集合
每个数字只能进一个集合
返回每个集合的平均值都累加起来的最小值
平均值向下取整
1 <= n <= 10^5
0 <= arr[i] <= 10^5
1 <= k <= n
来自真实大厂笔试，没有在线测试，对数器验证
'''
inf = int(1e18)
def solve():
    left, right = a[:k-1], a[k-1:]
    return sum(left) + sum(right) // len(right)
               
def naive():
    ans = inf
    def dfs(i: int, sets: int, pre: int, sum_avg: int):
        if sets > k or k - sets > n - i:
            return
        if i == n:
            nonlocal ans
            if sets == k and pre == n:
                ans = min(ans, sum_avg)
            return
        dfs(i + 1, sets, pre, sum_avg)
        dfs(i + 1, sets + 1, i + 1, sum_avg + sum(a[pre:i+1]) // (i - pre + 1))
    dfs(0, 0, 0, 0)
    return ans

import random, sys
sys.setrecursionlimit(int(5e4))
rnd = random.randint
print('測試開始')
for _ in range(5):
    k = rnd(2, 5)
    n = rnd(k + 1, 8)
    a = [rnd(1, 20) for _ in range(n)]
    a.sort()
    res_naive, res_solve = naive(), solve()
    if res_naive != res_solve:
        print(f'出錯了!! {res_naive} != {res_solve}')
        print(k, a)
    print('-------------------------')
print('測試結束')