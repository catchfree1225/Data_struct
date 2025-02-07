import sys
input = lambda: sys.stdin.readline().strip()
MII = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
from bisect import bisect_left

def solve():
    g = []
    for x in a:
        i = bisect_left(g, x + 1)
        if i == len(g):
            g.append(x)
        else:
            g[i] = x
    m = len(g)
    print(m + min(k, n - m))
               
for _ in range(1):
    n, k = MII()
    a = list(MII())
    solve()