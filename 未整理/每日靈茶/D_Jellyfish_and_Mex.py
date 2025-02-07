import sys
input = sys.stdin.readline

def solve():
    cnt = [0] * (n + 1)
    for x in a:
        if x < n:
            cnt[x] += 1
    mex = 0
    while cnt[mex] > 0:
        mex += 1
    
    ans = mex * (cnt[0] - 1) # 不用去除自己, 不然就去掉所有i
    f = [0] * mex # 定义 f[i] 表示在已经去掉所有 i 的情况下，后续操作的代价之和。
    for i in range(1, mex):
        f[i] = int(1e9) # 不用討論 mex =1
        for j, c in enumerate(cnt[:i]):
            f[i] = min(f[i], f[j] + i * c)
        ans = min(ans, f[i] + mex * (cnt[i] - 1))
    print(ans)
               
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    solve()
    