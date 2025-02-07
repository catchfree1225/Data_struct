import sys
input = lambda: sys.stdin.readline().strip()
MII = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())

def solve():
    a = []
    for _ in range(n):
        v, w, m = MII()
        i = 1
        while i <= m:
            a.append((w * i, v * i))
            m -= i
            i <<= 1
        if m:
            a.append((w * m, v * m))
    a.sort()
    
    f = [0] * (W + 1)
    hi = 0
    for w, v in a:
        hi += w
        for i in range(min(hi, W), w - 1, -1):
            f[i] = max(f[i], f[i - w] + v)
    print(f[W])
                
for _ in range(1):
    n, W = MII()
    solve()