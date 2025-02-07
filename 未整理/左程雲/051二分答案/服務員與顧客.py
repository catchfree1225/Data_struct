"""
Google面試題
给定一个数组arr,长度为n
表示n个服务员,每个人服务一位顧客的时间
给定一个正数m,表示有m个人等位
如果你是刚来的人，请问你需要等多久？
假设:m远远大于n,比如n<=1e3, m <= 1e8,该怎么做?
"""
def solve():
    def check(t: int) -> bool:
        return sum(t // x + 1 for x in arr) >= m
    
    l, r = -1, min(arr) * m + 1
    while l + 1 < r:
        mid = l + (r - l) // 2
        if check(mid):
            r = mid
        else:
            l = mid
    return r

from heapq import *
def checker():
    q = [(0, x) for x in arr]
    for _ in range(m):
        pend, t = heappop(q)
        heappush(q, (pend + t, t))
    return q[0][0] 


import random, time
for _ in range(1):
    def random_array():
        return [random.randint(l, r) for _ in range(n)]
    
    n, m = int(1e3), int(2e6)
    l, r = 1, int(250)
    print('=======================================')
    for i in range(50):
        print(f'第{i}次測試:')
        arr = random_array()
        # print(arr)
        t1, res1, t2 = time.time(), solve(), time.time()
        print(f'solve執行時間: {(t2 - t1) * 1000:.3f}ms')
        
        t1, res2, t2 = time.time(), checker(), time.time()
        print(f'check執行時間: {(t2 - t1) * 1000:.3f}ms')
        if res1 != res2:
            print(f'出錯啦! {res1} != {res2}')
        print('=======================================')
        
    print("測試結束")
    