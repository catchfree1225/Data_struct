import sys
input = lambda: sys.stdin.readline().strip()
MII = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
from bisect import bisect_left

def solve():
    pre, suf, g = [], [], []
    for x in a:
        i = bisect_left(g, x)
        pre.append(i + 1)
        if i == len(g):
            g.append(x)
        else:
            g[i] = x
    g = []
    for x in reversed(a):
        x *= -1
        i = bisect_left(g, x)
        suf.append(i + 1)
        if i == len(g):
            g.append(x)
        else:
            g[i] = x
    suf.reverse() # *-1 + rev.
    
    ans = [] 
    m = len(g) # LIS長度是固定的，看不同start與end
    cnt = [0] * (n + 1)
    for i in range(n):    
        if pre[i] + suf[i] - 1 == m:
            ans.append('2')
            cnt[pre[i]] += 1
        else:
            ans.append('1')
    for i, tp in enumerate(ans):
        if tp == '2' and cnt[pre[i]] == 1:
            ans[i] = '3'
    print(''.join(ans))
               
for _ in range(1):
    n = int(input())
    a = list(MII())
    solve()