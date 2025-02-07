import sys
input = sys.stdin.readline

def solve(a, l, r):
    for _ in range(1):
        # l, r = map(lambda x: int(x) - 1, input().split())
        if bucket[l] == bucket[r]:
            return(r - l + 1)
        else:
            l_cnt = right[bucket[l]] - l + 1
            r_cnt = r - left[bucket[r]] + 1
            mid_cnt = 0
            if bucket[l] + 1 < bucket[r]:
                fr, to = bucket[l] + 1, bucket[r] - 1
                p = (to - fr + 1).bit_length() - 1
                mid_cnt = max(st[fr][p], st[to - (1 << p) + 1][p])
            return(max(l_cnt, r_cnt, mid_cnt))
      
# for _ in range(1):
#     n, q = map(int, input().split())
#     a = list(map(int, input().split()))
#     solve()
#     _ = input()

from collections import Counter
def checker(a, l, r):
    ct = Counter(a[l:r+1])
    return max(ct.values())


import random, time
for _ in range(1):
    def random_array(l, r):
        return [random.randint(l, r) for _ in range(n)]
    
    n = int(1e6)
    a = sorted(random_array(-int(1e5), int(1e5)))
    # 建立st表
    bucket = [0] * n
    left, right = [0] * n, [n - 1] * n
    cnt = 0
    for i in range(n):
        bucket[i] = cnt
        if i < n - 1 and a[i] != a[i + 1]:
            right[cnt] = i
            left[cnt + 1] = i + 1
            cnt += 1
    del left[cnt+1:], right[cnt+1:]  

    k = cnt.bit_length() - 1
    st = [[0] * (k + 1) for _ in range(cnt + 1)]
    for i in range(cnt + 1):
        st[i][0] = right[i] - left[i] + 1
    for p in range(k):
        for i in range(cnt + 1 - (1 << p)):
            st[i][p + 1] = max(st[i][p], st[i + (1 << p)][p])
    
    print('=======================================')
    for i in range(500):
        print(f'第{i}次測試:')
        l = random.randint(1, n - 1)
        r = random.randint(l, n - 1)
        if l > r:
            l, r = r, l
        
        # print(arr)
        t1, res1, t2 = time.time(), solve(a, l, r), time.time()
        print(f'solve執行時間: {(t2 - t1) * 1000:.3f}ms')
        
        t1, res2, t2 = time.time(), checker(a, l, r), time.time()
        print(f'check執行時間: {(t2 - t1) * 1000:.3f}ms')
        if res1 != res2:
            print(a[l:r+1], l, r)
            print(f'出錯啦! {res1} != {res2}')
        print('=======================================')
        
    print("測試結束")
    