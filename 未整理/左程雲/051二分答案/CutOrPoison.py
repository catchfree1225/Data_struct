"""
怪兽的初始血量是一个整数hp，给出每一回合刀砍和毒杀的数值cuts和poisons
第i回合如果用刀砍，怪兽在这回合会直接损失cuts[i]的血，不再有后续效果
第i回合如果用毒杀，怪兽在这回合不会损失血量，但是之后每回合都损失poisons[i]的血量
并且你选择的所有毒杀效果，在之后的回合都会叠加
两个数组cuts、poisons，长度都是n，代表你一共可以进行n回合
每一回合你只能选择刀砍或者毒杀中的一个动作
如果你在n个回合内没有直接杀死怪兽，意味着你已经无法有新的行动了
但是怪兽如果有中毒效果的话，那么怪兽依然会在血量耗尽的那回合死掉
返回至少多少回合，怪兽会死掉
数据范围 : 
1 <= n <= 10^5; 1 <= hp <= 10^9; 1 <= cuts[i], poisons[i] <= 10^9
"""
def solve():
    def check(t: int) -> bool:
        need = hp
        for i in range(min(n, t)):
            d_cut = cuts[i]
            d_poison = poisons[i] * (t - i)
            need -= max(d_cut, d_poison)
            if need <= 0:
                return True
        return False
    
    l, r = -1, int(1e3)
    while l + 1 < r:
        mid = l + (r - l) // 2
        if check(mid):
            r = mid
        else:
            l = mid
    return r

from functools import cache
def checker():
    @cache
    def dfs(i: int, need: int, poi: int):
        need -= poi
        if need <= 0:
            return i
        if i == n:
            return i + (need + poi - 1) // poi if poi else int(1e10)
                      
        r_cut = dfs(i + 1, need - cuts[i], poi)
        r_poison = dfs(i + 1, need, poi + poisons[i])
        return min(r_cut, r_poison)
    return dfs(0, hp, 0)


import random, time
for _ in range(1):
    def random_array():
        return [random.randint(l, r) for _ in range(n)]
    
    n, hp = int(1e3), int(1e6)
    l, r = int(1), int(5e4)
    print('=======================================')
    for i in range(100):
        print(f'第{i}次測試:')
        cuts = random_array()
        poisons = random_array()
        t1, res1, t2 = time.time(), solve(), time.time()
        print(f'solve執行時間: {(t2 - t1) * 1000:.3f}ms')
        
        t1, res2, t2 = time.time(), checker(), time.time()
        print(f'check執行時間: {(t2 - t1) * 1000:.3f}ms')
        if res1 != res2:
            print(f'出錯啦! {res1} != {res2}')
        print('=======================================')
        
    print("測試結束")
    