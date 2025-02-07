'''
题目3
组团买票
景区里一共有m个项目，景区的第i个项目有如下两个参数:
game[i] = { Ki, Bi }，Ki、Bi一定是正数
Ki代表折扣系数，Bi代表票价，举个例子 : Ki = 2, Bi = 10
如果只有1个人买票，单张门票的价格为 : Bi - Ki * 1 = 8
所以这1个人游玩该项目要花8元
如果有2个人买票，单张门票的价格为 : Bi - Ki * 2 = 6
所以这2个人游玩该项目要花6 * 2 = 12元
如果有5个人买票，单张门票的价格为 : Bi - Ki * 5 = 0
所以这5个人游玩该项目要花5 * 0 = 0元
如果有更多人买票，都认为花0元(因为让项目倒贴钱实在是太操蛋了)
于是可以认为，如果有x个人买票，单张门票的价格为 : Bi - Ki * x
x个人游玩这个项目的总花费是 : max { x * (Bi - Ki * x), 0 }
单位一共有n个人，每个人最多可以选1个项目来游玩，也可以不选任何项目，由你去按照上面的规则，统一花钱购票
你想知道自己需要准备多少钱，就可以应付所有可能的情况，返回这个最保险的钱数
1 <= M、N、Ki、Bi <= 10^5
来自真实大厂笔试，没有在线测试，对数器验证
'''
from heapq import heappop, heappush, heapify
def solve():
    h = []
    def calc(ki, bi, pi):
        return bi - (pi + 1) * ki - pi * ki
    for ki, bi in ps:
        earn = calc(ki, bi, 0)
        h.append((-earn, ki, bi, 0))
    heapify(h)
    ans = 0
    for _ in range(n): # 一次選一個
        earn, ki, bi, pi = heappop(h)
        if -earn <= 0:
            break
        ans += -earn
        pi += 1
        earn = calc(ki, bi, pi)
        heappush(h, (-earn, ki, bi, pi))
    return ans
               
def naive():
    ans = set()
    def dfs(i: int, tot: int, val: int):
        # 也可以不选任何项目
        ans.add(val)
        if i == m or tot == n:
            return
        ki, bi = ps[i]
        for j in range(n - tot + 1):
            price = max(j * (bi - ki * j), 0)
            dfs(i + 1, tot + j, val + price)
    dfs(0, 0, 0)
    return max(ans)

import random, sys
sys.setrecursionlimit(int(5e4))
rnd = random.randint
print('測試開始')
for _ in range(5):
    m = rnd(1, 8)
    n = rnd(1 + m // 2, 50)
    ps = [(rnd(10, 20), rnd(200, 300)) for _ in range(m)]
    res_naive, res_solve = naive(), solve()
    if res_naive != res_solve:
        print(f'出錯了!! {res_naive} != {res_solve}')
    print('-------------------------')
print('測試結束')