'''
题目5
执行所有任务的最少初始电量
每一个任务有两个参数，需要耗费的电量、至少多少电量才能开始这个任务
返回手机至少需要多少的初始电量，才能执行完所有的任务
来自真实大厂笔试，没有在线测试，对数器验证
'''
inf = int(1e18)
def solve():
    a = sorted(ori_A, key=lambda x: x[1] - x[0])
    ans = 0
    for cost, req in a:
        ans = max(ans + cost, req)
    return ans

def naive():
    path, perm = [], []
    def dfs(vis: int):
        if vis == (1 << n) - 1:
            perm.append(path.copy())
            return
        for i in range(n):
            if vis >> i & 1 == 0:
                path.append(ori_A[i])
                dfs(vis | 1 << i)
                path.pop()
    dfs(0)
    ans = inf
    for ai in perm:
        res = 0
        for cost, req in ai:
            res = max(res + cost, req)
        ans = min(ans, res)
    return ans

import random, sys
sys.setrecursionlimit(int(5e4))
rnd = random.randint
print('測試開始')
for _ in range(5):
    n = rnd(2, 8)
    ori_A = [(rnd(1, 20), rnd(21, 40)) for _ in range(n)]
    res_naive, res_solve = naive(), solve()
    if res_naive != res_solve:
        print(f'出錯了!! {res_naive} != {res_solve}')
        print(ori_A)
    print('-------------------------')
print('測試結束')