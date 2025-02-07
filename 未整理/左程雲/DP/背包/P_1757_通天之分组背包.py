from collections import defaultdict
import sys
input = lambda: sys.stdin.readline().strip()
MII = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())

def solve():
    a = defaultdict(list)
    for _ in range(n):
        c, w, i = MII()
        a[i].append((c, w))
        
    items = [[] for _ in range(len(a))]
    for i, gi in a.items():
        gi.sort(key=lambda x: (x[0], -x[1]))
        pre = None
        for c, w in gi:
            if pre == c:
               continue
            pre = c
            items[i - 1].append((c, w))
    
    f = [0] * (m + 1)
    hi = 0
    for gi in items:
        hi += gi[-1][0]
        for j in range(m, -1, -1):
            for c, w in gi:
                if c > j: break
                f[j] = max(f[j], f[j - c] + w)
    print(f[m])
               
for _ in range(1):
    m, n = MII()
    solve()