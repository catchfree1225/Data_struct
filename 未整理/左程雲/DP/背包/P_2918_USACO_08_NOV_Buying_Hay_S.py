from math import inf
import sys
input = lambda: sys.stdin.readline().strip()
MII = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())

def solve():
    ori_A = [list(MII()) for _ in range(n)]
    ori_A.sort(key=lambda x: (x[1], -x[0]))
    a, pre = [], None
    for w, c in ori_A:
        if pre != c:
            pre = c
            a.append((w, c))
    
    cap = h + max(w for w, _ in a) # 至少再買一個物品
    f = [inf] * (cap + 1)
    f[0] = 0
    for w, c in a:
        for i in range(w, cap + 1):
            f[i] = min(f[i], f[i - w] + c)
    print(min(f[h:]))
               
for _ in range(1):
    n, h = MII()
    solve()