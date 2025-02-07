import sys
input = lambda: sys.stdin.readline().strip()
MII = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())

def solve():
    f = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n - 1, -1, -1):
        v, w = a[i]
        for j in range(m + 1):
            f[i][j] = f[i + 1][j]
            if j >= v:
                f[i][j] = max(f[i][j], f[i + 1][j - v] + w)
    
    ans = []
    j = m
    for i in range(n):
        v, w = a[i]
        if j >= v and f[i][j] == f[i + 1][j - v] + w:
            ans.append(i + 1)
            j -= v
    print(*ans)
                
            
for _ in range(1):
    n, m = MII()
    a = [tuple(MII()) for _ in range(n)]
    solve()