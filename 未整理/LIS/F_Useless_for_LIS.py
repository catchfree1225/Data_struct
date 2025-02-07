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
    for i in range(n):    
        if pre[i] + suf[i] - 1 == m:
            ans.append(i + 1)
    print(len(ans))
    print(*ans)
               
for _ in range(int(input())):
    n = int(input())
    a = list(MII())
    solve()